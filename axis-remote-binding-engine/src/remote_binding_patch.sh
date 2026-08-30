#!/bin/bash
# ==============================================================================
# AXIS-TCET Robust Remote Binding Patch
# Ensures origin remote existence check before updating or setting URL.
# ==============================================================================

set -euo pipefail

REPO_NAME="houston-identity-registry"
GITHUB_USER="SUPRANODE00"
REMOTE_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"

echo "[*] Verifying git remote configuration states..."
if git remote | grep -q "^origin$"; then
    echo "[*] Existing 'origin' detected. Updating remote URL..."
    git remote set-url origin "$REMOTE_URL"
else
    echo "[*] No 'origin' found. Initializing new remote binding..."
    git remote add origin "$REMOTE_URL"
fi

echo "[*] Executing upstream push to branch main..."
git push -u origin main

echo "[+] Remote synchronization verified. Ground state secured."
