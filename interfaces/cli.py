def emit_event(events):
    for e in events:
        print(f"[EVENT] t={e['time']} signal={e['signal']}")
