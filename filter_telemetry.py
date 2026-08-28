import json
from pathlib import Path

telemetry_file = Path.home() / ".local" / "log" / "origin_emitter" / "mesh_telemetry.jsonl"

print(f"[*] Aggregating and filtering telemetry streams from: {telemetry_file}\n")
if telemetry_file.exists():
    sessions = {}
    with open(telemetry_file, "r") as f:
        for line in f:
            if line.strip():
                record = json.loads(line)
                seq = record['sequence']
                # Keep the latest or group by transmission timestamp
                sessions[record['transmission_timestamp_ns']] = record

    sorted_timestamps = sorted(sessions.keys())
    print(f"Total Unique Frames Captured: {len(sorted_timestamps)}")
    for ts in sorted_timestamps[-10:]:
        rec = sessions[ts]
        print(f"Timestamp: {ts} | Seq: {rec['sequence']} | Vector: {rec['orientation_vector']} | Polarity: {rec['polarity_state']}")
else:
    print("[!] Telemetry stream file not found.")
