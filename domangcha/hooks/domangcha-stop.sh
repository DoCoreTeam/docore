#!/usr/bin/env bash
# Claude Stop adapter. Canonical validation is deterministic and runtime-neutral.
set -u

PROJECT_ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
ENGINE=""

if [ -f "$PROJECT_ROOT/domangcha/engine.py" ]; then
    ENGINE="$PROJECT_ROOT/domangcha/engine.py"
elif [ -f "$HOME/.domangcha/domangcha/engine.py" ]; then
    ENGINE="$HOME/.domangcha/domangcha/engine.py"
fi

[ -z "$ENGINE" ] && exit 0

# Repository metadata validation applies only to the DOMANGCHA source repo.
if [ -f "$PROJECT_ROOT/domangcha/VERSION" ] && [ -f "$PROJECT_ROOT/package.json" ]; then
    OUTPUT=$(python3 "$ENGINE" validate --root "$PROJECT_ROOT" 2>&1)
    STATUS=$?
    if [ "$STATUS" -ne 0 ]; then
        echo "[DOMANGCHA STOP VALIDATION FAILED]" >&2
        echo "$OUTPUT" >&2
        exit 2
    fi
fi

exit 0
