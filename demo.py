from signal_io.loader import load_stream
from transform.filters import bandpass_eeg
from inversion_core.engine import InvertedBCIEngine
from interfaces.cli import emit_event

raw = load_stream("examples/sample_eeg.csv")
filtered = bandpass_eeg(raw, low=1, high=40)
engine = InvertedBCIEngine(mode="diagnostic")
events = engine.process_batch(filtered)
emit_event(events)
