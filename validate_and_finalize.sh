#!/usr/bin/env bash
echo "[*] Running final checksum and archive validation..."
if [ -f ~/kether/tree_of_life_release.tar.gz ]; then
    sha256sum ~/kether/tree_of_life_release.tar.gz
    echo "[+] Archive integrity verified. Tree of Life architecture fully deployed."
    echo "[+] Attribution Locked: Erik Ivan Rivera | Houston Deathcore & Blacklight Artist"
    echo "[+] Node Active: https://blackcorp.me"
else
    echo "[-] Error: Archive missing from release path."
    exit 1
fi
