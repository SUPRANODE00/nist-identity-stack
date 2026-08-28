import subprocess

def dump_active_journal():
    print("[*] Dumping active systemd journal logs including daemon stdout...")
    result = subprocess.run(
        ["journalctl", "--user", "-u", "origin_mesh.service", "-n", "20", "--no-pager"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result.stdout)

if __name__ == "__main__":
    dump_active_journal()
