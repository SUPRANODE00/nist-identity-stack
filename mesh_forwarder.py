import socket
import json
from pathlib import Path

snapshot_file = Path.home() / ".local" / "log" / "origin_emitter" / "mesh_snapshot_latest.json"

def forward_mesh():
    if not snapshot_file.exists():
        print("[!] Snapshot file missing.")
        return

    with open(snapshot_file, "r") as f:
        payload = f.read()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # Broadcast locally and reflect to loopback gateway target
    targets = [('<broadcast>', 5005), ('127.0.0.1', 5005)]
    for target in targets:
        sock.sendto(payload.encode('utf-8'), target)
        print(f"[MESH FORWARD] Dispatched payload to {target[0]}:{target[1]}")
    
    sock.close()
    print("[SUCCESS] Mesh forward operation complete.")

if __name__ == "__main__":
    forward_mesh()
