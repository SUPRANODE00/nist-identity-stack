#!/usr/bin/env bash
# CAPSULECRAFT // TRANSCEIVER PIPELINE CONTROLLER

CONFIG_FILE="./transceiver_state.json"
DB_PATH="./telemetry_events.db"

# Initialize state configuration if missing
if [[ ! -f "$CONFIG_FILE" ]]; then
    cat <<'JSON' > "$CONFIG_FILE"
{
  "carrier_freq_ghz": 1.420,
  "spatial_radius_m": 500,
  "origin_lat": 29.620000,
  "origin_lon": -95.230000,
  "failover_active": false
}
JSON
fi

adjust_freq() {
    local delta="$1"
    local current_freq
    current_freq=$(jq '.carrier_freq_ghz' "$CONFIG_FILE")
    local new_freq
    new_freq=$(awk -v curr="$current_freq" -v d="$delta" 'BEGIN { printf "%.3f", curr + d }')
    sed -i "s/\"carrier_freq_ghz\": $current_freq/\"carrier_freq_ghz\": $new_freq/" "$CONFIG_FILE"
    echo "[+] Frequency shifted to ${new_freq} GHz"
}

adjust_sweep() {
    local new_radius="$1"
    local current_radius
    current_radius=$(jq '.spatial_radius_m' "$CONFIG_FILE")
    sed -i "s/\"spatial_radius_m\": $current_radius/\"spatial_radius_m\": $new_radius/" "$CONFIG_FILE"
    echo "[+] Radius updated to ${new_radius}m"
}

trigger_failover() {
    sed -i 's/"failover_active": false/"failover_active": true/' "$CONFIG_FILE"
    echo "[!] Disaster recovery failover active."
}

case "$1" in
    [Aa]) adjust_freq "${2:-0.050}" ;;
    [Rr]) adjust_sweep "${2:-1000}" ;;
    [Ss]) trigger_failover ;;
    *) echo "Usage: $0 { A [step] | R [radius] | S }" ; exit 1 ;;
esac
