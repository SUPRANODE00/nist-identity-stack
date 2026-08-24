import socket
import json
import time
import sqlite3

HOST = "0.0.0.0"
PORT = 8088
DB_FILE = "telemetry_events.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS telemetry_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            msisdn TEXT,
            node_alias TEXT,
            radius_m INTEGER,
            lat REAL,
            lon REAL,
            compartment_id TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_telemetry(ts, msisdn, alias, radius, coords, comp_id):
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        lat = coords[0] if len(coords) >= 1 else 0.0
        lon = coords[1] if len(coords) >= 2 else 0.0
        c.execute("""
            INSERT INTO telemetry_logs 
            (timestamp, msisdn, node_alias, radius_m, lat, lon, compartment_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (ts, msisdn, alias, radius, lat, lon, comp_id))
        conn.commit()
        conn.close()
        return True
    except Exception as err:
        print(f"[-] DB WRITE ERROR: {err}")
        return False

def main():
    init_db()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    print(f"[*] VINCULUM MAN Gateway + SQLite Logger listening on {HOST}:{PORT}...")

    while True:
        try:
            data, addr = sock.recvfrom(4096)
            payload = json.loads(data.decode('utf-8'))
            
            header = payload.get("header", {})
            auth = payload.get("auth", {})
            origin = payload.get("origin_node", {})
            
            org = header.get("organization")
            domain = auth.get("org_domain")
            msisdn = origin.get("msisdn")
            alias = origin.get("node_alias")
            radius = origin.get("radius_coverage_m")
            coords = origin.get("spatial_coordinates", [0.0, 0.0])
            comp_id = payload.get("network_compartment", {}).get("compartment_id")
            
            if org == "VINCULUM" and domain == "vinculum.blackcorp.me":
                now = int(time.time())
                db_saved = save_telemetry(now, msisdn, alias, radius, coords, comp_id)
                
                print(f"[+] VALID PACKET RECEIVED from {addr[0]}:{addr[1]}")
                print(f"    - Target MSISDN: {msisdn}")
                print(f"    - Alias: {alias}")
                print(f"    - Radius Coverage: {radius}m")
                print(f"    - Coordinates: {coords}")
                print(f"    - SQLite Status: {'STORED' if db_saved else 'FAILED'}")
                
                ack_response = {
                    "header": {
                        "organization": "VINCULUM",
                        "msg_type": "LINK_RADIUS_ACK",
                        "timestamp_epoch": now
                    },
                    "status": "SUCCESS",
                    "linked_msisdn": msisdn,
                    "assigned_compartment": comp_id
                }
                
                sock.sendto(json.dumps(ack_response).encode('utf-8'), addr)
                print(f"[+] ACK sent back to {addr[0]}:{addr[1]}\n")
            else:
                print(f"[-] DISCARDED: Unauthorized payload from {addr[0]} (Org: {org}, Domain: {domain})\n")

        except Exception as e:
            print(f"[-] Error parsing incoming transmission: {e}")

if __name__ == "__main__":
    main()
