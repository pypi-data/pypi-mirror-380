#!/bin/sh

# Finds the absolute path of the script
SCRIPT_DIR=$(dirname "$0")
PROJECT_ROOT=$(cd "$SCRIPT_DIR/../../" && pwd)

# Hook paths
HOOKS_SRC="$PROJECT_ROOT/scripts/git-hooks/hooks"
HOOKS_DEST="$PROJECT_ROOT/.git/hooks"

# Create .git/hooks folder if it doesn't exist
mkdir -p "$HOOKS_DEST"

# Copy shell hooks
cp "$HOOKS_SRC"/* "$HOOKS_DEST/"

# Makes hooks executable
chmod +x "$HOOKS_DEST"/*

echo "Done."
