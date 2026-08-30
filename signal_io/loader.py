def load_stream(path):
    # For now, just read CSV lines into a list
    with open(path) as f:
        return [line.strip().split(",") for line in f.readlines()]
