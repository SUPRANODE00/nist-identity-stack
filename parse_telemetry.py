import json
from pathlib import Path

telemetry_file = Path.home() / ".local" / "log" / "origin_emitter" / "mesh_telemetry.jsonl"

print(f"[*] Reading telemetry records from: {telemetry_file}\n")
if telemetry_file.exists():
    with open(telemetry_file, "r") as f:
        for line in f:
            if line.strip():
                record = json.loads(line)
                print(f"Node: {record['node_id']} | Seq: {record['sequence']} | Vector: {record['orientation_vector']} | Polarity: {record['polarity_state']}")
else:
    print("[!] Telemetry file not found.")
