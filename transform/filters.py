def bandpass_eeg(raw, low=1, high=40):
    # Stub: return only rows where channel 2 is within range
    return [row for row in raw[1:] if row[1].isdigit() and low <= int(row[1]) <= high]
