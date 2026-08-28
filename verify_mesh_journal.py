import subprocess

def check_journal():
    print("[*] Inspecting systemd journal logs for origin_mesh.service...")
    result = subprocess.run(
        ["journalctl", "--user", "-u", "origin_mesh.service", "-n", "10", "--no-pager"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result.stdout)

if __name__ == "__main__":
    check_journal()
