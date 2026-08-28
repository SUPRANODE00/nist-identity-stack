#!/usr/bin/env bash
LOG_DIR="$HOME/.local/log/origin_emitter"
mkdir -p "$LOG_DIR"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "[*] Initializing Origin-Vector Emitter at $TIMESTAMP" | tee -a "$LOG_DIR/system.log"

CLOCK_HZ=1000
POLARITY_STATE="POSITIVE_UP"

echo "[+] Setting Clock Source: ${CLOCK_HZ}Hz"
echo "[+] Establishing Polarity: $POLARITY_STATE"

if command -v octave &> /dev/null && [ -f "origin_matrix.m" ]; then
    octave --eval "run('origin_matrix.m'); disp('Matrix Grid Compiled Successfully.');"
else
    echo "[!] MATLAB/Octave engine or origin_matrix.m not detected in path. Running fallback Python engine."
    python3 emitter_core.py
fi

while true; do
    PULSE_ID=$(date +%s%N)
    echo "[$TIMESTAMP] PULSE_EMITTED ID: $PULSE_ID | POLARITY: $POLARITY_STATE" >> "$LOG_DIR/pulse_stream.log"
    sleep 1
done
