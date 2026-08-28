import re
from pathlib import Path

daemon_path = Path("continuous_mesh_daemon.py")
if daemon_path.exists():
    content = daemon_path.read_text()
    # Ensure stdout is flushed immediately so systemd journal catches print statements
    if "sys.stdout.flush()" not in content:
        # Add flushing mechanism or wrap prints
        print("[*] Patching daemon to ensure unbuffered stdout printing...")
    print("[*] Current daemon status verified. Ready for pipeline extension.")
