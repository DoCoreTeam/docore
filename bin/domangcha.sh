#!/usr/bin/env bash
set -e

VERSION="3.0.2"
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

USAGE:
  domangcha [OPTIONS]

There is no install-mode flag. One command decides what this directory needs:

  in a project        installs the project loop here — offline, never writes to ~/.claude
  outside a project   installs the harness into ~/.claude and ~/.domangcha
  /ceo needs more     the loop offers to bring the harness in, only when you ask for it

OPTIONS:
  --lang ko|en    language for the protocol documents and the loop CLI (default ko)
  --no-migrate    keep an existing CLAUDE.md in place instead of moving it
                  to .claude/heavy/CEO.md
  --agents        also create AGENTS.md and GEMINI.md symlinks to LOOP.md
  --version, -v   print version and exit
  --help, -h      show this help message and exit

MORE INFO:
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
  echo "domangcha v${VERSION} — 하네스 설치 / installing the harness into ~/.claude"
  echo ""
  curl -fsSL "${INSTALL_URL}" | bash
}

install_loop() {
  if ! command -v node >/dev/null 2>&1; then
    echo "domangcha: the project loop needs Node 22.13+." >&2
    echo "Install Node, or run this outside a project to install the harness instead." >&2
    exit 1
  fi
  node "${SCRIPT_DIR}/domangcha-loop.mjs" "$@"
  if [ -f "$HARNESS" ]; then
    echo "  이 머신에는 하네스도 설치돼 있습니다 / the harness is also installed on this machine"
    echo "  갱신 / refresh it:  curl -fsSL ${INSTALL_URL} | bash"
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
      echo "  (run this from a project directory to install the project loop there)"
      echo ""
      install_harness
    fi
    ;;
  *)
    echo "Unknown option: $1" >&2
    echo "Run 'domangcha --help' for usage." >&2
    exit 1
    ;;
esac
