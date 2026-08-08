#!/usr/bin/env bash
set -e

VERSION="2.1.0"
INSTALL_URL="https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh"

usage() {
  cat <<EOF
domangcha v${VERSION} — AI getaway car from development hell

USAGE:
  domangcha [OPTIONS]

OPTIONS:
  --version   Print version and exit
  --help      Show this help message and exit

DESCRIPTION:
  Installs DOMANGCHA adaptive DIRECT/LOOP/GRAPH execution for Claude Code
  and OpenAI Codex. Runs the official install script from GitHub.

INSTALL:
  npx domangcha
  OR
  curl -fsSL ${INSTALL_URL} | bash

MORE INFO:
  https://github.com/DoCoreTeam/domangcha
EOF
}

case "${1:-}" in
  --version|-v)
    echo "domangcha v${VERSION}"
    exit 0
    ;;
  --help|-h)
    usage
    exit 0
    ;;
  "")
    echo "domangcha v${VERSION} — Installing..."
    echo ""
    curl -fsSL "${INSTALL_URL}" | bash
    ;;
  *)
    echo "Unknown option: $1" >&2
    echo "Run 'domangcha --help' for usage." >&2
    exit 1
    ;;
esac
