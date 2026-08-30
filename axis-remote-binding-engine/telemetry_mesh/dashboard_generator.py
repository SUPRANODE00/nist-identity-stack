#!/usr/bin/env python3
import os
import json
from datetime import datetime

def generate_dashboard():
    print("[*] Generating AXIS-TCET Continuum Status Dashboard...")
    
    metrics_path = "reports/mesh_metrics_summary.json"
    topology_path = "config/mesh_topology.json"
    
    metrics = {}
    if os.path.exists(metrics_path):
        with open(metrics_path, "r") as f:
            metrics = json.load(f)
            
    topology = {}
    if os.path.exists(topology_path):
        with open(topology_path, "r") as f:
            topology = json.load(f)
            
    dashboard_content = f"""# AXIS-TCET Continuum Status Dashboard

**Generated:** {datetime.utcnow().isoformat()}Z  
**Continuum:** {metrics.get('mesh_continuum', 'AXIS-TCET')}  
**System Status:** `{metrics.get('status', 'unknown').upper()}`  
**Active Architecture:** {topology.get('architecture', 'Undefined')} (Sequence {topology.get('sequence', 'N/A')})  

## Active Mesh Nodes
"""

    for node in topology.get('nodes', []):
        dashboard_content += f"- **{node['id']}** | Role: `{node['role']}` | State: `{node['status']}`\n"

    dashboard_content += f"\n## Audit Metrics\n- Total Audits Recorded: `{metrics.get('total_audits_found', 0)}`\n"

    output_path = "reports/CONTINUUM_STATUS.md"
    with open(output_path, "w") as f:
        f.write(dashboard_content)
        
    print(f"[+] Status dashboard compiled successfully at {output_path}")

if __name__ == "__main__":
    generate_dashboard()
