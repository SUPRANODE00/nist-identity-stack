import time
import subprocess
from pathlib import Path

log_dir = Path.home() / ".local" / "log" / "origin_emitter"
log_dir.mkdir(parents=True, exist_ok=True)
pulse_log = log_dir / "pulse_stream.log"

print(f"[*] Starting Origin-Vector Emitter Daemon. Logging to {pulse_log}")

seq = 0
try:
    while True:
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        pulse_id = time.time_ns()
        log_entry = f"[{timestamp}] PULSE_EMITTED ID: {pulse_id} | POLARITY: POSITIVE_UP | SEQ: {seq}\n"
        
        with open(pulse_log, "a") as f:
            f.write(log_entry)
            
        print(f"Emitted & Logged -> Seq: {seq} | ID: {pulse_id}")
        seq += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[INFO] Daemon stopped by operator.")
