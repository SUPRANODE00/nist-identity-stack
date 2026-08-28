import socket
import time

def verify_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', 5005))
    sock.settimeout(6.0)
    
    print("[*] Listening on UDP port 5005 for live telemetry frames...", flush=True)
    try:
        data, addr = sock.recvfrom(65535)
        print(f"[SUCCESS] Received live frame from {addr}:", flush=True)
        print(data.decode('utf-8')[:300], flush=True)
    except socket.timeout:
        print("[!] Timeout waiting for broadcast frame.", flush=True)
    finally:
        sock.close()

if __name__ == "__main__":
    verify_listener()
