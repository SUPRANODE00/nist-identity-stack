import subprocess
import time
from pathlib import Path

def configure_service():
    service_path = Path.home() / ".config" / "systemd" / "user" / "origin_mesh.service"
    service_path.parent.mkdir(parents=True, exist_ok=True)
    
    script_path = Path.cwd() / "continuous_mesh_daemon.py"
    python_path = subprocess.check_output(["which", "python3"]).decode("utf-8").strip()
    
    service_content = f"""[Unit]
Description=Origin Mesh Telemetry Synchronization Daemon
After=network.target

[Service]
ExecStart={python_path} {script_path}
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=default.target
"""
    
    with open(service_path, "w") as f:
        f.write(service_content)
        
    print(f"[SUCCESS] Systemd user service written to: {service_path}")
    print("[*] Reloading systemd user daemon and enabling service...")
    
    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    subprocess.run(["systemctl", "--user", "enable", "origin_mesh.service"], check=True)
    subprocess.run(["systemctl", "--user", "restart", "origin_mesh.service"], check=True)
    
    print("[SUCCESS] Mesh telemetry background service is now persistent.")
    time.sleep(2.0)
    subprocess.run(["systemctl", "--user", "status", "origin_mesh.service", "--no-pager"])

if __name__ == "__main__":
    configure_service()
