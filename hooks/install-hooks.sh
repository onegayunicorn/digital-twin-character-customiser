#!/usr/bin/env bash
# install-hooks.sh — symlink the repo git hooks into .git/hooks
set -euo pipefail

HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GIT_HOOKS="$(git rev-parse --git-dir)/hooks"

mkdir -p "$GIT_HOOKS"

for hook in pre-commit commit-msg pre-push post-merge; do
  if [ -f "$HOOK_DIR/$hook" ]; then
    ln -sf "$HOOK_DIR/$hook" "$GIT_HOOKS/$hook"
    echo "✔ installed hook: $hook"
  fi
done

echo "Git hooks installed. (npm run hooks:install re-runs this.)"
