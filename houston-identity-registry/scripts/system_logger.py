import json
import os
from datetime import datetime, timezone

def log_system_state():
    state_data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operator": "SUPRANODE00",
        "environment": "Terminal / Linux Container",
        "status": "Operational",
        "telemetry_link": "Active"
    }
    
    os.makedirs("audits", exist_ok=True)
    file_path = "audits/latest_state.json"
    
    with open(file_path, 'w') as f:
        json.dump(state_data, f, indent=4)
        
    print(f"[LOGGED] System state successfully captured at {file_path}")

if __name__ == "__main__":
    log_system_state()
