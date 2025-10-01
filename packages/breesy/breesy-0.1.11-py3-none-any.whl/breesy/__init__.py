"""Breesy - Brainwave Retrieval, Extraction, and Easy Signal Yield.

Breesy provides easy-to-use functions and pipelines for neuroscience students
who want to apply signal processing and statistical methods on EEG data.
"""

__version__ = '0.1.0'

# Import core classes
from .Recording import Recording
from .Event import Event
from .RecordingMetadata import RecordingMetadata

# Make key modules and functions available at package level
from . import events, load, constants, features, type_hints, errors, \
    signal_generation, processing, plots, transform, data, load_events
