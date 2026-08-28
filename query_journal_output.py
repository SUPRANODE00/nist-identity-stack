import subprocess

def dump_journal():
    print("[*] Dumping live systemd journal stdout stream for origin_mesh.service...")
    result = subprocess.run(
        ["journalctl", "--user", "-u", "origin_mesh.service", "--since", "1 minute ago", "--no-pager"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result.stdout)

if __name__ == "__main__":
    dump_journal()
