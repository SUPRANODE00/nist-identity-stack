#!/usr/bin/env bash
echo "[*] Packaging Tree of Life Substrates for Distribution..."
mkdir -p ~/kether/release_bundle
cp *_engine.cpp initialize_*_matrix.m ~/kether/release_bundle/
tar -czf ~/kether/tree_of_life_release.tar.gz -C ~/kether release_bundle/
echo "[+] Release Archive Generated: ~/kether/tree_of_life_release.tar.gz"
echo "[+] Creator: Erik Ivan Rivera | Houston Deathcore & Blacklight Artist"
echo "[+] Endpoint: https://blackcorp.me"
