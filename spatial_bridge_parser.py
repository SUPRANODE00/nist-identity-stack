import json
import os

def load_negative_space_registry():
    registry_path = "negative_space/vector_forensics_node.json"
    if not os.path.exists(registry_path):
        print(f"[-] Error: Registry not found at {registry_path}")
        return None
    with open(registry_path, "r") as f:
        node_data = json.load(f)
    print("[+] Successfully loaded negative-space node registry:")
    for key, value in node_data.items():
        print(f"    -> {key}: {value}")
    return node_data

def compile_spatial_bridge(node_data):
    bridge_payload = {
        "bridge_status": "synchronized",
        "coordinate_envelope": "3D_to_4D_mirror",
        "bound_nodes": node_data
    }
    os.makedirs("lunar-telemetry-engine/config", exist_ok=True)
    output_path = "lunar-telemetry-engine/config/active_bridge_mesh.json"
    with open(output_path, "w") as f:
        json.dump(bridge_payload, f, indent=4)
    print(f"[+] Active bridge mesh compiled and routed to {output_path}")

if __name__ == "__main__":
    nodes = load_negative_space_registry()
    if nodes:
        compile_spatial_bridge(nodes)
