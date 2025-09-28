import numpy as np

from .Event import Event
from .RecordingMetadata import RecordingMetadata
from .errors import BreesyError
from .type_hints import enforce_type_hints


class Recording:
    """Represents an EEG recording with data, channel information, and events."""

    data: np.ndarray
    """EEG data array of shape (channels, samples)"""

    channel_names: list[str]
    """List of channel names"""

    sample_rate: int | float
    """Sampling rate in Hz"""

    events: list[Event] | None
    """List of Event objects"""

    metadata: RecordingMetadata | None
    """Additional metadata about the recording"""

    @enforce_type_hints
    def __init__(self,
                 data: np.ndarray,
                 channel_names: list[str],
                 sample_rate: int | float,
                 events: list[Event] | None = None,
                 metadata: RecordingMetadata | None = None, ):
        """Initialize a Recording.

        :param data: EEG data array of shape (channels, samples)
        :param channel_names: List of channel names
        :param sample_rate: Sampling rate in Hz
        :param events: List of Event objects
        :param metadata: Additional metadata about the recording
        """

        if data.ndim != 2:
            raise BreesyError(
                "The EEG data provided has an incorrect number of dimensions. Expected data.ndim to be 2, but got "
                f"{data.ndim} dimensions instead.",
                "The data provided is likely not EEG data, or there are several records joined into one file. However, Breesy only supports ordinary two-dimensional EEG data for now."
            )

        n_channels, n_samples = data.shape
        if (n_channels != len(channel_names)) and (n_samples != len(channel_names)):
            raise BreesyError(
                f"The number of channel names ({len(channel_names)}) provided does not match the "
                f"number of channels ({n_channels}) in the EEG data.",
                "Make sure that the number of channel names provided matches the number of channels in the EEG data."
                "You can see the number of channel names like this: len(eeg_channel_names)."
            )
        elif (n_channels != len(channel_names)) and (n_samples == len(channel_names)):
            print('Warning: data rows and columns will be switched places according to the provided channel names.')
            self.data = data.T
        else:
            self.data = data

        self.channel_names = channel_names

        if sample_rate <= 0:
            raise BreesyError(
                f"Sample rate should be more than 0, but you provided {sample_rate}.",
                "Make sure that the sample rate is a positive integer. E.g., a sample rate of: 512."
            )

        is_typical_sample_rate = 100 < sample_rate < 5000
        if not is_typical_sample_rate:
            print(f"Warning: Unusual sample rate ({sample_rate} Hz). Typical EEG sample rates range from 128-2000 Hz.")
        self.sample_rate = sample_rate

        if events is None:
            events = []
        self._set_events(events)

        self.metadata = metadata

    def _set_events(self, events: list[Event]) -> None:
        out_of_range_events = [event for event in events if event.index >= self.number_of_samples]
        if out_of_range_events:
            raise BreesyError(
                f"Found {len(out_of_range_events)} events with indices out of range for the provided EEG data. "
                f"First Got index {out_of_range_events[0].index} while the EEG data has {self.number_of_samples} samples.",
                "Make sure that the event indices are within the range of the EEG data. "
                "For instance, if the EEG data has 10000 samples, the event indices should be less than 10000. "
                "You can see the number of samples in the EEG data like so: eeg_data.shape[1]."
            )

        sorted_events = sorted(events, key=lambda event: event.index)
        self.events = sorted_events

    def __repr__(self):
        """Return a string representation of the Recording object."""
        metadata_repr = f", name={self.metadata.name}" if self.metadata else ""
        events_repr = f", event_count={len(self.events)}" if self.events else ""
        return (f"Recording("
                f"channels={self.number_of_channels}, "
                f"duration={self.duration:.2f} s, "
                f"sample_rate={self.sample_rate} Hz"
                f"{metadata_repr}"
                f"{events_repr}"
                f")")


    @property
    def number_of_channels(self):
        """Return the number of channels in the recording."""
        return self.data.shape[0]

    @property
    def duration(self):
        """Return the duration of the recording in seconds."""
        return self.data.shape[1] / self.sample_rate

    @property
    def number_of_samples(self):
        """Return the number of samples in the recording."""
        return self.data.shape[1]
