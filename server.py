import json
import os
from fastapi import FastAPI, HTTPException

app = FastAPI(title="AXIS Telemetry Bridge API", version="1.0.0")

TELEMETRY_PACKET_PATH = "lunar-telemetry-engine/config/mqtt_stream_packet.json"

@app.get("/")
def read_root():
    return {
        "status": "active",
        "node_origin": "SUPRANODE00",
        "domain": "api.blackcorp.me",
        "envelope": "3D_to_4D_mirror"
    }

@app.get("/telemetry/stream")
def get_telemetry_stream():
    if not os.path.exists(TELEMETRY_PACKET_PATH):
        raise HTTPException(status_code=404, detail="Telemetry stream packet not found.")
    
    with open(TELEMETRY_PACKET_PATH, "r") as f:
        packet_data = json.load(f)
        
    return {
        "status": "success",
        "ingress_source": "Mosquitto MQTT local bridge",
        "data": packet_data
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
