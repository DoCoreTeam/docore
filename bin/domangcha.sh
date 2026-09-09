#!/usr/bin/env bash
set -e

VERSION="3.0.4"
INSTALL_URL="https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh"

# npm links bin entries as symlinks, so resolve the real file before locating siblings.
resolve_script_dir() {
  local src="${BASH_SOURCE[0]}" dir
  while [ -L "$src" ]; do
    dir="$(cd -P "$(dirname "$src")" && pwd)"
    src="$(readlink "$src")"
    case "$src" in /*) ;; *) src="$dir/$src" ;; esac
  done
  cd -P "$(dirname "$src")" && pwd
}
SCRIPT_DIR="$(resolve_script_dir)"
HARNESS="${HOME}/.domangcha/domangcha/engine.py"

usage() {
  cat <<EOF
domangcha v${VERSION} — AI getaway car from development hell
                       개발 지옥에서 도망쳐

USAGE / 사용법:
  domangcha [OPTIONS]

  Run it, do not add it as a dependency. Use npx, or pnpm dlx / yarn dlx.
  설치하지 말고 실행하세요. npx, pnpm 이나 Yarn 이면 pnpm dlx / yarn dlx.

There is no install-mode flag. One command decides what this directory needs.
설치 방식을 고르는 플래그는 없습니다. 한 명령이 이 자리에 필요한 것을 판단합니다.

  in a project        installs the project loop here — offline, never writes to ~/.claude
  프로젝트 안         이 자리에 루프 설치 — 오프라인, ~/.claude 무접촉

  outside a project   installs the harness into ~/.claude and ~/.domangcha
  프로젝트 밖         ~/.claude 와 ~/.domangcha 에 하네스 설치

  /ceo needs more     the loop offers to bring the harness in, only when you ask for it
  /ceo 로 요청하면    루프가 하네스 설치를 제안합니다, 요청했을 때만

OPTIONS / 옵션:
  --lang ko|en    language for the protocol documents and the loop CLI (default ko)
                  프로토콜 문서와 루프 CLI 의 언어 (기본 ko)
  --no-migrate    keep an existing CLAUDE.md in place instead of moving it to .claude/heavy/CEO.md
                  기존 CLAUDE.md 를 .claude/heavy/CEO.md 로 옮기지 않고 그 자리에 둠
  --agents        also create AGENTS.md and GEMINI.md symlinks to LOOP.md
                  AGENTS.md, GEMINI.md 를 LOOP.md 로 심볼릭 링크
  --version, -v   print version and exit / 버전 출력 후 종료
  --help, -h      show this help message and exit / 이 도움말 출력 후 종료

UPDATING / 업데이트:
  run the same command again; the loop CLI is refreshed and your rule files are kept
  같은 명령을 다시 실행하면 루프 CLI 만 갱신되고 규정 파일은 보존됩니다

MORE INFO / 더 보기:
  https://github.com/DoCoreTeam/domangcha
EOF
}

# A directory counts as a project when it carries a repository or a manifest.
is_project() {
  [ -d .git ] || [ -f package.json ] || [ -f pyproject.toml ] || [ -f go.mod ] \
    || [ -f Cargo.toml ] || [ -f pom.xml ] || [ -f build.gradle ] || [ -f build.gradle.kts ] \
    || [ -f Gemfile ] || [ -f composer.json ] || [ -f Makefile ] || [ -f CMakeLists.txt ]
}

install_harness() {
  echo "domangcha v${VERSION} — installing the harness into ~/.claude"
  echo "                 ~/.claude 에 하네스를 설치합니다"
  echo ""
  curl -fsSL "${INSTALL_URL}" | bash
}

install_loop() {
  if ! command -v node >/dev/null 2>&1; then
    echo "domangcha: the project loop needs Node 22.13+." >&2
    echo "           프로젝트 루프에는 Node 22.13 이상이 필요합니다." >&2
    echo "Install Node, or run this outside a project to install the harness instead." >&2
    echo "Node 를 설치하거나, 프로젝트 밖에서 실행해 하네스를 설치하세요." >&2
    exit 1
  fi
  node "${SCRIPT_DIR}/domangcha-loop.mjs" "$@"
  if [ -f "$HARNESS" ]; then
    echo "  the harness is also installed on this machine"
    echo "  이 머신에는 하네스도 설치돼 있습니다"
    echo "  refresh it / 갱신:  curl -fsSL ${INSTALL_URL} | bash"
  fi
}

case "${1:-}" in
  --version|-v) echo "domangcha v${VERSION}" ;;
  --help|-h)    usage ;;
  ""|--no-migrate|--agents|--lang)
    if is_project; then
      install_loop "$@"
    else
      echo "domangcha: not inside a project, so installing the harness."
      echo "           프로젝트 안이 아니므로 하네스를 설치합니다."
      echo "  run this from a project directory to install the project loop there"
      echo "  프로젝트 폴더에서 실행하면 그 프로젝트에 루프를 설치합니다"
      echo ""
      install_harness
    fi
    ;;
  *)
    echo "Unknown option: $1" >&2
    echo "알 수 없는 옵션: $1" >&2
    echo "Run 'domangcha --help' for usage. / 사용법은 domangcha --help" >&2
    exit 1
    ;;
esac
