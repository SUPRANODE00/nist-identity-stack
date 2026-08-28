import re
from pathlib import Path

daemon_path = Path("continuous_mesh_daemon.py")
if daemon_path.exists():
    code = daemon_path.read_text()
    
    # Check if print statements need flush=True injection
    if "print(" in code and "flush=True" not in code:
        print("[*] Upgrading daemon print calls with flush=True for real-time journal capture...")
        # Replace print(...) with print(..., flush=True) safely
        updated_code = re.sub(r'print\((.*?)\)', r'print(\1, flush=True)', code)
        daemon_path.write_text(updated_code)
        print("[SUCCESS] Daemon code updated.")
    
    # Restart the user service to load changes
    import subprocess
    print("[*] Restarting origin_mesh.service to apply updates...")
    subprocess.run(["systemctl", "--user", "restart", "origin_mesh.service"], check=True)
    print("[SUCCESS] Service restarted successfully.")
