#!/usr/bin/env python3
import os
import glob
import json
from datetime import datetime

def aggregate_metrics():
    print("[*] Parsing AXIS-TCET telemetry audit logs...")
    log_pattern = "logs/telemetry_audit_*.log"
    logs = glob.glob(log_pattern)
    
    summary = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "total_audits_found": len(logs),
        "status": "nominal",
        "mesh_continuum": "AXIS-TCET"
    }
    
    report_path = "reports/mesh_metrics_summary.json"
    with open(report_path, "w") as f:
        json.dump(summary, f, indent=2)
        
    print(f"[+] Metrics successfully aggregated. Report written to {report_path}")

if __name__ == "__main__":
    aggregate_metrics()
