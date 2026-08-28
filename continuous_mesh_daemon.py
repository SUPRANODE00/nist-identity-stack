import socket
import json
import time
from pathlib import Path

snapshot_file = Path.home() / ".local" / "log" / "origin_emitter" / "mesh_snapshot_latest.json"

def run_daemon():
    print("[*] Initializing continuous mesh background telemetry daemon...", flush=True)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    targets = [('<broadcast>', 5005), ('127.0.0.1', 5005)]
    
    try:
        while True:
            if snapshot_file.exists():
                with open(snapshot_file, "r") as f:
                    payload = f.read()
                
                for target in targets:
                    sock.sendto(payload.encode('utf-8'), target)
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                print(f"[DAEMON] Dispatched synchronization heartbeat frame at {timestamp}", flush=True)
            else:
                print("[!] Snapshot source file missing. Retrying...", flush=True)
            
            time.sleep(5.0)
    except KeyboardInterrupt:
        print("\n[!] Daemon terminated by operator.", flush=True)
    finally:
        sock.close()

if __name__ == "__main__":
    run_daemon()
