import time
import json
from pathlib import Path

class MeshTelemetryBridge:
    def __init__(self):
        self.log_dir = Path.home() / ".local" / "log" / "origin_emitter"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.telemetry_file = self.log_dir / "mesh_telemetry.jsonl"

    def pack_telemetry(self, seq: int, vector: float, polarity: str):
        packet = {
            "node_id": "ORIGIN-VECTOR-EMITTER-01",
            "sequence": seq,
            "orientation_vector": vector,
            "polarity_state": polarity,
            "grid_mesh_origin": {"x": 0.0, "y": 0.0, "z": 0.0},
            "transmission_timestamp_ns": time.time_ns()
        }
        return packet

    def broadcast_loop(self):
        print(f"[MESH] Telemetry bridge active. Writing frames to {self.telemetry_file}")
        seq = 0
        try:
            while seq < 10:
                packet = self.pack_telemetry(seq, round(float(seq) * 0.1, 4), "POSITIVE_UP")
                with open(self.telemetry_file, "a") as f:
                    f.write(json.dumps(packet) + "\n")
                print(f"[MESH SYNC] Frame Dispatched -> Seq: {seq} | Vector: {packet['orientation_vector']}")
                seq += 1
                time.sleep(0.5)
        except Exception as e:
            print(f"[ERROR] Mesh transmission interrupted: {e}")

if __name__ == "__main__":
    bridge = MeshTelemetryBridge()
    bridge.broadcast_loop()
