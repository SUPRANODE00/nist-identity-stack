import socket
import json

def listen_for_mesh():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', 5005))

    print("[*] Listening for incoming mesh snapshot broadcasts on UDP port 5005...")
    try:
        data, addr = sock.recvfrom(65535)
        print(f"[RECV] Packet received from {addr[0]}:{addr[1]} ({len(data)} bytes)")
        
        snapshot = json.loads(data.decode('utf-8'))
        print(f"Node Origin: {snapshot.get('node_origin')}")
        print(f"Snapshot Status: {snapshot.get('snapshot_status')}")
        print(f"Total Frames Indexed: {snapshot.get('total_frames_indexed')}")
        print("Active Session Frame Vectors:")
        for frame in snapshot.get('active_session_frames', []):
            print(f"  -> Seq: {frame['sequence']} | Vector: {frame['orientation_vector']} | Polarity: {frame['polarity_state']}")
    except Exception as e:
        print(f"[!] Error handling packet: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    listen_for_mesh()
