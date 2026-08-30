#!/usr/bin/env python3
import time
import os
from datetime import datetime, timezone

def capture_infra_metrics():
    log_file = "infra-signal-sweep.log"
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    load_avg = os.getloadavg()
    line = f"[{timestamp}] INFRA-METRIC: Load={load_avg}, Status=SECURE_ACTIVE\n"
    with open(log_file, "a") as f:
        f.write(line)
    print(line.strip())

if __name__ == "__main__":
    while True:
        capture_infra_metrics()
        time.sleep(60)
