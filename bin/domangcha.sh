#!/usr/bin/env bash
set -e

VERSION="3.0.0"
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

usage() {
  cat <<EOF
domangcha v${VERSION} — AI getaway car from development hell

USAGE:
  domangcha [OPTIONS]

DEFAULT (no options):
  Installs the lightweight autonomous loop into the CURRENT project directory.
  Writes LOOP.md, CLAUDE.md, scripts/loop.mjs, .claude/, .cursor/, and .loop/.
  Never touches ~/.claude. Requires Node 22.13+.

OPTIONS:
  --full, heavy   Install the full 18-agent harness globally into ~/.claude
                  (the v2.x behaviour, unchanged)
  --no-migrate    Keep an existing CLAUDE.md in place instead of moving it
                  to .claude/heavy/CEO.md
  --agents        Also create AGENTS.md and GEMINI.md symlinks to LOOP.md
  --version, -v   Print version and exit
  --help, -h      Show this help message and exit

INSTALL:
  npx domangcha             # lightweight, per project
  npx domangcha --full      # full 18-agent harness, global

MORE INFO:
  https://github.com/DoCoreTeam/domangcha
EOF
}

install_full() {
  echo "domangcha v${VERSION} — 전체 18 에이전트 설치 / Installing full harness..."
  echo ""
  curl -fsSL "${INSTALL_URL}" | bash
}

install_loop() {
  if ! command -v node >/dev/null 2>&1; then
    echo "domangcha: Node 22.13+ is required for the lightweight loop." >&2
    echo "Install Node, or run 'domangcha --full' for the global harness." >&2
    exit 1
  fi
  exec node "${SCRIPT_DIR}/domangcha-loop.mjs" "$@"
}

case "${1:-}" in
  --version|-v)
    echo "domangcha v${VERSION}"
    ;;
  --help|-h)
    usage
    ;;
  --full|heavy|full)
    install_full
    ;;
  ""|--no-migrate|--agents)
    install_loop "$@"
    ;;
  *)
    echo "Unknown option: $1" >&2
    echo "Run 'domangcha --help' for usage." >&2
    exit 1
    ;;
esac
