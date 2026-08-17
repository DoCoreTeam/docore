#!/usr/bin/env bash
# ============================================================
# DOMANGCHA PostToolUse Hook — Auto-Test + Auto-Fix
# Triggered after: Write | Edit | MultiEdit
# ============================================================
INPUT=$(cat)

# ── Extract file path from hook JSON ──────────────────────
FILE_PATH=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    ti = d.get('tool_input', {})
    print(ti.get('file_path', '') or ti.get('path', ''))
except:
    print('')
" 2>/dev/null || echo "")

[ -z "$FILE_PATH" ] && exit 0
[ ! -f "$FILE_PATH" ] && exit 0

# Skip non-source files (docs, configs, locks)
case "$FILE_PATH" in
    *.md|*.txt|*.json|*.yaml|*.yml|*.toml|*.lock|*.env*|*.log) exit 0 ;;
esac

# ── Find project root ──────────────────────────────────────
find_root() {
    local dir
    dir=$(dirname "$FILE_PATH")
    # Stop at $HOME: above it a stray package.json is not this file's project.
    while [ "$dir" != "/" ] && [ "$dir" != "$HOME" ]; do
        for m in package.json go.mod Cargo.toml requirements.txt pyproject.toml pom.xml build.gradle; do
            [ -f "$dir/$m" ] && { echo "$dir"; return; }
        done
        dir=$(dirname "$dir")
    done
    dirname "$FILE_PATH"
}
PROJECT_ROOT=$(find_root)

# ── Detect test runner ─────────────────────────────────────
detect_runner() {
    if [ -f "$PROJECT_ROOT/package.json" ]; then
        grep -q '"vitest"' "$PROJECT_ROOT/package.json" 2>/dev/null && { echo "vitest"; return; }
        grep -q '"jest"'   "$PROJECT_ROOT/package.json" 2>/dev/null && { echo "jest";   return; }
        echo "npm"
    elif [ -f "$PROJECT_ROOT/go.mod" ];      then echo "go"
    elif [ -f "$PROJECT_ROOT/Cargo.toml" ];  then echo "cargo"
    elif [ -f "$PROJECT_ROOT/requirements.txt" ] || [ -f "$PROJECT_ROOT/pyproject.toml" ]; then echo "pytest"
    elif [ -f "$PROJECT_ROOT/pom.xml" ];     then echo "maven"
    elif [ -f "$PROJECT_ROOT/build.gradle" ]; then echo "gradle"
    else echo "unknown"
    fi
}
RUNNER=$(detect_runner)
[ "$RUNNER" = "unknown" ] && exit 0

# ── Find related test file ─────────────────────────────────
BASE=$(basename "$FILE_PATH" | sed 's/\.[^.]*$//')
FILE_DIR=$(dirname "$FILE_PATH")

find_test() {
    for pattern in \
        "$FILE_DIR/${BASE}.test.*"       "$FILE_DIR/${BASE}.spec.*" \
        "$FILE_DIR/__tests__/${BASE}.*"  "${PROJECT_ROOT}/__tests__/${BASE}.*" \
        "${PROJECT_ROOT}/tests/test_${BASE}.*" \
        "${PROJECT_ROOT}/tests/${BASE}_test.*"; do
        for f in $pattern; do
            [ -f "$f" ] && { echo "$f"; return; }
        done
    done
}
TEST_FILE=$(find_test)

# ── Run tests ──────────────────────────────────────────────
run_test() {
    cd "$PROJECT_ROOT"
    case "$RUNNER" in
        vitest) [ -n "$TEST_FILE" ] && npx vitest run "$TEST_FILE" 2>&1 || npx vitest run --passWithNoTests 2>&1 ;;
        jest)   [ -n "$TEST_FILE" ] && npx jest "$(basename "$TEST_FILE")" --no-coverage --silent 2>&1 \
                                     || npx jest --no-coverage --silent --passWithNoTests 2>&1 ;;
        npm)    npm test 2>&1 ;;
        pytest) [ -n "$TEST_FILE" ] && python -m pytest "$TEST_FILE" -x -q 2>&1 || exit 0 ;;
        go)
            PKG=$(python3 -c "import os; print('./'+os.path.relpath('$(dirname "$FILE_PATH")', '$PROJECT_ROOT'))" 2>/dev/null || echo "./...")
            go test "$PKG" 2>&1 ;;
        cargo)  cargo test 2>&1 ;;
        maven)  mvn test -q 2>&1 ;;
        gradle) ./gradlew test 2>&1 ;;
    esac
}

TEST_OUTPUT=$(run_test 2>&1)
TEST_EXIT=$?
[ $TEST_EXIT -eq 0 ] && exit 0

# Return deterministic feedback to the active runtime. Never spawn a nested
# model process from a hook: retries belong to LOOP/GRAPH execution state.
echo "[DOMANGCHA VALIDATION FAILED] $FILE_PATH" >&2
echo "$TEST_OUTPUT" >&2
exit 2
