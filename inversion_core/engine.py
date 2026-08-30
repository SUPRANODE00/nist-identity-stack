class InvertedBCIEngine:
    def __init__(self, mode="diagnostic"):
        self.mode = mode

    def process_batch(self, features):
        # Stub: just wrap features in events
        return [{"time": f[0], "signal": f[1:]} for f in features]
