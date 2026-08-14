#!/usr/bin/env bash
# make hook scripts executable (run once after clone)
chmod +x "$(dirname "${BASH_SOURCE[0]}")"/pre-commit
chmod +x "$(dirname "${BASH_SOURCE[0]}")"/commit-msg
chmod +x "$(dirname "${BASH_SOURCE[0]}")"/pre-push
chmod +x "$(dirname "${BASH_SOURCE[0]}")"/post-merge
chmod +x "$(dirname "${BASH_SOURCE[0]}")"/install-hooks.sh
echo "✔ hook scripts are executable"
