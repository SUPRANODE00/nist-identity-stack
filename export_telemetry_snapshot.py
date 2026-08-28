import json
from pathlib import Path

log_dir = Path.home() / ".local" / "log" / "origin_emitter"
telemetry_file = log_dir / "mesh_telemetry.jsonl"
snapshot_file = log_dir / "mesh_snapshot_latest.json"

print(f"[*] Compiling snapshot state from: {telemetry_file}")
if telemetry_file.exists():
    frames = []
    with open(telemetry_file, "r") as f:
        for line in f:
            if line.strip():
                frames.append(json.loads(line))
    
    # Sort by timestamp and retain latest session window (last 10 frames)
    frames_sorted = sorted(frames, key=lambda x: x['transmission_timestamp_ns'])
    latest_session = frames_sorted[-10:]
    
    snapshot_payload = {
        "node_origin": "ORIGIN-VECTOR-EMITTER-01",
        "snapshot_status": "SYNCHRONIZED",
        "total_frames_indexed": len(frames_sorted),
        "active_session_frames": latest_session
    }
    
    with open(snapshot_file, "w") as sf:
        json.dump(snapshot_payload, sf, indent=4)
        
    print(f"[SUCCESS] Snapshot exported to: {snapshot_file}")
    print(json.dumps(snapshot_payload, indent=2))
else:
    print("[!] Telemetry stream not found.")
