import socket
import json
from pathlib import Path

snapshot_file = Path.home() / ".local" / "log" / "origin_emitter" / "mesh_snapshot_latest.json"

def broadcast_snapshot():
    if not snapshot_file.exists():
        print("[!] Snapshot file missing. Export state first.")
        return

    with open(snapshot_file, "r") as f:
        payload = f.read()

    # Setup UDP socket for local mesh broadcast
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    broadcast_addr = ('<broadcast>', 5005)
    print(f"[*] Broadcasting mesh snapshot (size: {len(payload)} bytes) to UDP port 5005...")
    sock.sendto(payload.encode('utf-8'), broadcast_addr)
    sock.close()
    print("[SUCCESS] Mesh snapshot broadcast complete.")

if __name__ == "__main__":
    broadcast_snapshot()
