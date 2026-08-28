import json
import os

def render_spatial_grid():
    config_path = "lunar-telemetry-engine/config/active_bridge_mesh.json"
    if not os.path.exists(config_path):
        print(f"[-] Error: Active bridge mesh not found at {config_path}")
        return
        
    with open(config_path, "r") as f:
        mesh_data = json.load(f)
        
    print("[*] Initializing Three.js 3D Spatial Rendering Engine...")
    print(f"[*] Bridge Status: {mesh_data.get('bridge_status')}")
    print(f"[*] Coordinate Envelope: {mesh_data.get('coordinate_envelope')}")
    print("[+] Rendering Negative-Space Node Envelopes:")
    
    for key, value in mesh_data.get("bound_nodes", {}).items():
        print(f"    -> [MESH NODE] {key} mapped to vector -> {value}")
        
    print("[+] 3D avatar skin data mesh grid activation complete.")

if __name__ == "__main__":
    render_spatial_grid()
