import time
import math

class OriginVectorEmitter:
    def __init__(self, clock_source_hz: int):
        self.clock_hz = clock_source_hz
        self.interval = 1.0 / clock_source_hz
        self.polarity = 1.0

    def emit_pulse(self, sequence: int):
        orientation_vector = math.sin(sequence * self.interval) * self.polarity
        signal_type = "SIGNAL" if orientation_vector >= 0 else "NOISE"
        return {
            "seq": sequence,
            "vector": round(orientation_vector, 4),
            "polarity": self.polarity,
            "type": signal_type,
            "timestamp": time.time_ns()
        }

if __name__ == "__main__":
    emitter = OriginVectorEmitter(clock_source_hz=10)
    print("[INFO] Origin-Vector Emitter Core Active.")
    for i in range(5):
        pulse = emitter.emit_pulse(i)
        print(f"Emitter Output -> Seq: {pulse['seq']} | Vector: {pulse['vector']} | Classification: {pulse['type']}")
        time.sleep(0.1)
