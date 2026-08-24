#!/usr/bin/env bash
CONFIG_FILE="./transceiver_state.json"
MQTT_HOST="localhost"
MQTT_PORT="1883"
MQTT_TOPIC="capsulecraft/transceiver/node44"

echo "[*] Watching $CONFIG_FILE for live modifications..."

while true; do
    inotifywait -e modify "$CONFIG_FILE" >/dev/null 2>&1
    
    carrier=$(jq '.carrier_freq_ghz' "$CONFIG_FILE")
    radius=$(jq '.spatial_radius_m' "$CONFIG_FILE")
    lat=$(jq '.origin_lat' "$CONFIG_FILE")
    lon=$(jq '.origin_lon' "$CONFIG_FILE")
    failover=$(jq '.failover_active' "$CONFIG_FILE")

    payload=$(cat <<JSON
{
  "node_id": "0x44",
  "carrier_freq_ghz": $carrier,
  "spatial_radius_m": $radius,
  "origin_lat": $lat,
  "origin_lon": $lon,
  "failover_active": $failover,
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
JSON
)
    echo "$payload" | mosquitto_pub -h "$MQTT_HOST" -p "$MQTT_PORT" -t "$MQTT_TOPIC" -l
done
