import socket
import json
import time

def listen_live():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', 5005))
    sock.settimeout(12.0)

    print("[*] Listening for active service heartbeat packets on port 5005...")
    try:
        while True:
            data, addr = sock.recvfrom(65535)
            snapshot = json.loads(data.decode('utf-8'))
            print(f"[{time.strftime('%H:%M:%S')}] LIVE RECV from {addr[0]} | Node: {snapshot.get('node_origin')} | Status: {snapshot.get('snapshot_status')} | Frames: {snapshot.get('total_frames_indexed')}")
    except socket.timeout:
        print("[!] Timeout reached without packet capture.")
    finally:
        sock.close()

if __name__ == "__main__":
    listen_live()
