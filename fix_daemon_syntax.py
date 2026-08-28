from pathlib import Path

daemon_path = Path("continuous_mesh_daemon.py")
if daemon_path.exists():
    code = daemon_path.read_text()
    
    # Fix the incorrectly placed flush=True inside strftime
    fixed_code = code.replace(
        "time.strftime('%Y-%m-%d %H:%M:%S', flush=True)",
        "time.strftime('%Y-%m-%d %H:%M:%S'), flush=True"
    )
    
    daemon_path.write_text(fixed_code)
    print("[SUCCESS] Fixed print statement syntax in continuous_mesh_daemon.py.")

import subprocess
subprocess.run(["systemctl", "--user", "restart", "origin_mesh.service"], check=True)
print("[SUCCESS] Restarted origin_mesh.service.")
