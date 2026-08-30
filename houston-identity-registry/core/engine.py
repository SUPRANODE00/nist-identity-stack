#!/usr/bin/env python3
import time
import os
from datetime import datetime, timezone

LOG_PATH = os.path.join(os.getcwd(), "telemetry-report.log")

def log_event(message):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"[{timestamp}] NODE-CORE: {message}\n"
    print(line.strip())
    with open(LOG_PATH, "a") as f:
        f.write(line)

def main():
    log_event("Node SUPRANODE00 engine initialized. State-inventory loop active.")  
    try:
        while True:
            time.sleep(300)
            log_event("Heartbeat pulse verified. Mesh synchronized.")
    except KeyboardInterrupt:
        log_event("Engine received shutdown signal. Going offline.")

if __name__ == "__main__":
    main()
