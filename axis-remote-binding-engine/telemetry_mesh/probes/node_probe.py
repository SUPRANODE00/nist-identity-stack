#!/usr/bin/env python3
import json
import os

def run_diagnostic():
    print("[*] Executing AXIS-TCET node telemetry health check...")
    config_path = "../config/mesh_topology.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            data = json.load(f)
        print(f"[+] Loaded Continuum: {data['continuum']} | Sequence: {data['sequence']}")
        for node in data['nodes']:
            print(f"    - Node ID: {node['id']} | Role: {node['role']} | Status: {node['status']}")
    else:
        print("[!] Topology configuration not found in local context.")

if __name__ == "__main__":
    run_diagnostic()
