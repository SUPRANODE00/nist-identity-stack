#!/usr/bin/env bash
set -euo pipefail

echo "[*] Executing AXIS-TCET State Verification Pipeline..."
mkdir -p logs

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
LOG_FILE="logs/telemetry_audit_${TIMESTAMP}.log"

echo "=== AXIS-TCET Audit Run: $TIMESTAMP ==" > "$LOG_FILE"
echo "[+] Invoking Node Probe..." | tee -a "$LOG_FILE"
python3 probes/node_probe.py | tee -a "$LOG_FILE"

echo "[+] Invoking Telemetry Orchestrator..." | tee -a "$LOG_FILE"
python3 orchestrator.py | tee -a "$LOG_FILE"

echo "[+] Audit complete. Log archived to $LOG_FILE"
