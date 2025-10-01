import matplotlib.pyplot as plt
import numpy as np

from .Recording import Recording
from .errors import BreesyError
from .constants import CLASSIC_BANDWIDTHS, EEG_MONTAGES
from .processing import get_frequency_spectrum, get_ica_components
from .transform import select_channels, remove_channels, select_bandwidth, cut_by_second_range
from .type_hints import enforce_type_hints


# -------- signal plots


@enforce_type_hints
def plot_recording(recording: Recording, omit_channels: list[str] | None = None,
                   start: float | int = 0.0, duration: float | int = 60.0, padding: float | int = 1.0) -> None:
    """Plot EEG signals with channels spread vertically.

    :param recording: Input EEG recording
    :param omit_channels: List of channel names to exclude from plotting
    :param start: Start time in seconds for the plot window
    :param duration: Duration in seconds to plot
    :param padding: Vertical spacing multiplier between channels
    """

    # TODO: add event visualization?
    if omit_channels:
        subrecording = remove_channels(recording, omit_channels)
    else:
        subrecording = recording
    _plot_signal(data=subrecording.data, sample_rate=subrecording.sample_rate, channel_names=subrecording.channel_names, 
                 start=start, duration=duration, padding=padding)
    plt.show()


@enforce_type_hints
def plot_recording_channels(recording: Recording, channel_names: list[str],
                            start: float | int = 0.0, duration: float | int = 60.0, padding: float | int = 1.0) -> None:
    """Plot EEG signals for selected channels only.

    :param recording: Input EEG recording
    :param channel_names: List of channel names to include in the plot
    :param start: Start time in seconds for the plot window
    :param duration: Duration in seconds to plot
    :param padding: Vertical spacing multiplier between channels
    """

    subrecording = select_channels(recording, channel_names)
    _plot_signal(data=subrecording.data, sample_rate=subrecording.sample_rate, channel_names=subrecording.channel_names, 
                 start=start, duration=duration, padding=padding)
    plt.show()


@enforce_type_hints
def plot_decomposed_signal(recording: Recording, omit_channels: list[str] | None = None,
                           single_channel: str | None = None, 
                           start: float | int = 0, duration: float | int = 3.0,
                           bandwidths: dict[str, tuple[float, float]] | None = None,
                           cmap: str = 'Dark2', cmap_size: int = 8) -> None:
    """Plot recording signal decomposed into frequency bands.

    :param recording: Input recording
    :param omit_channels: Name of channels to not be plotted
    :param single_channel: Single channel to plot (ignores omit_channels if set)
    :param start: From which second to start the plot
    :param duration: How many seconds to plot
    :param bandwidths: Dictionary of band names and frequency ranges
    :param cmap: Colormap name to use
    :param cmap_size: Number of colors to use from colormap
    """

    if bandwidths is None:
        bandwidths = CLASSIC_BANDWIDTHS   

    if single_channel is not None:
        subrecording = select_channels(recording, [single_channel])
        if omit_channels:
            print('Ignoring the omit_channels paramters because single_channel was set.')
    elif omit_channels:
        subrecording = remove_channels(recording, omit_channels)
    else:
        subrecording = recording

    start_sample = int(start * subrecording.sample_rate)
    n_samples = int(duration * subrecording.sample_rate)
    time = np.arange(n_samples) / subrecording.sample_rate + start

    fig, axes = plt.subplots(len(bandwidths), 1, figsize=(12, 2*len(bandwidths)), sharex=True, sharey=True)
    
    for (name, (low, high)), ax in zip(bandwidths.items(), axes):
        color_cycle = _get_color_cycle(cmap=cmap, cmap_size=cmap_size)
        filtered = select_bandwidth(subrecording, low, high)
        for i in range(len(subrecording.channel_names)):
            ax.plot(time, filtered.data[i, start_sample:n_samples+start_sample], lw=1, alpha=0.8, color=next(color_cycle))
        ax.set_title(f'{name} ({low}-{high} Hz)')
        ax.set_xlim(start, duration+start)
        ax.grid(True)

    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.show()


# -------- frequency plots


@enforce_type_hints
def plot_mean_frequency_spectrum(recording: Recording, omit_channels: list[str] | None = None,
                                 color: str = '#aa0000', ax: plt.Axes | None = None) -> None:
    """Plot mean frequency spectrum calculated from all channels. Method used: periodogram.

    :param recording: Input EEG recording
    :param omit_channels: List of channel names to exclude from the plot
    :param color: Color for the spectrum line
    :param ax: Matplotlib axes to plot on. If None, creates new figure
    """

    if omit_channels:
        subrecording = remove_channels(recording, omit_channels)
    else:
        subrecording = recording

    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 4))
    ax.grid(True)
    plt.box(False)

    f, periodograms = get_frequency_spectrum(subrecording)
    mean_periodogram = periodograms.mean(axis=0)
    geom_mean = np.exp(np.mean(np.log(mean_periodogram)))

    ax.semilogy(f, mean_periodogram, lw=1, color=color)
    ax.set_title(f'Mean periodogram of {len(subrecording.channel_names)} EEG channels')
    ax.set_ylim(geom_mean**2 / mean_periodogram.max(), mean_periodogram.max())
    ax.set_xlim(0, subrecording.sample_rate / 2)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Power')
    plt.show()


@enforce_type_hints
def plot_frequency_spectrum(recording: Recording, omit_channels: list[str] | None = None,
                            cmap: str = 'Dark2', cmap_size: int = 8, ax: plt.Axes | None = None) -> None:
    """Plot frequency spectrum for all channels in one plot. Method used: periodogram.

    :param recording: Input EEG recording
    :param omit_channels: List of channel names to exclude from the plot
    :param cmap: Colormap name for channel coloring
    :param cmap_size: Number of colors to use from the colormap
    :param ax: Matplotlib axes to plot on. If None, creates new figure
    """

    if omit_channels:
        subrecording = remove_channels(recording, omit_channels)
    else:
        subrecording = recording

    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 4))
    ax.grid(True)
    plt.box(False)

    f, periodograms = get_frequency_spectrum(subrecording)
    geom_mean = np.mean(np.exp(np.mean(np.log(periodograms), axis=1)))

    nch = len(subrecording.channel_names)
    color_cycle = _get_color_cycle(cmap=cmap, cmap_size=cmap_size)
    for i in range(nch):
        ax.semilogy(f, periodograms[i], lw=1, color=next(color_cycle), alpha=max(0.2, min(2/nch, 0.9)))
    ax.set_title(f'Periodogram ({nch} EEG channels)')
    ax.set_xlim(0, subrecording.sample_rate / 2)
    ax.set_ylim(geom_mean**2 / periodograms.max(), periodograms.max())
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Power')
    plt.show()


# ---- montage plots


@enforce_type_hints
def plot_recording_electrodes(recording: Recording, hide_unused: bool = True,
                              figsize: tuple[int, int] = (8, 8), head_radius: float | int = 1.0,
                              head_color: str = "white", edge_color: str = "black",
                              electrode_color: str = "beige", electrode_highlight_color: str = "#fcb001",
                              fontsize: str | int = "medium", ax: plt.Axes | None = None) -> None:
    """Plot electrode montage showing electrode positions for the recording channels.

    :param recording: Input EEG recording
    :param hide_unused: Whether to hide electrodes not present in the recording
    :param figsize: Figure size as (width, height) in inches
    :param head_radius: Radius of the head outline
    :param head_color: Fill color for the head outline
    :param edge_color: Color for head outline and electrode borders
    :param electrode_color: Default color for electrodes
    :param electrode_highlight_color: Color for highlighted electrodes
    :param fontsize: Font size for electrode labels
    :param ax: Matplotlib axes to plot on. If None, creates new figure
    """

    montage_name = _detect_montage_type(recording.channel_names)
    locations = _get_locations_for_montage(montage_name)

    _plot_electrode_montage(
        locations=locations, electrode_names=recording.channel_names,
        hide_unused=hide_unused, figsize=figsize, head_radius=head_radius,
        head_color=head_color, edge_color=edge_color,
        electrode_color=electrode_color, electrode_highlight_color=electrode_highlight_color,
        fontsize=fontsize, ax=ax
    )


@enforce_type_hints
def plot_default_montage(montage: str = "10-10",
                         head_radius: float | int = 1.0, figsize: tuple[int, int] = (8, 8),
                         head_color: str = 'white', edge_color: str = 'black', electrode_color: str = 'lightgrey',
                         fontsize: str | int = 'medium', ax: plt.Axes | None = None) -> None:
    """Plot a standard EEG electrode montage.

    :param montage: EEG montage system ('10-10' or '10-20')
    :param head_radius: Radius of the head outline
    :param figsize: Figure size as (width, height) in inches
    :param head_color: Fill color for the head outline
    :param edge_color: Color for head outline and electrode borders
    :param electrode_color: Color for electrode markers
    :param fontsize: Font size for electrode labels
    :param ax: Matplotlib axes to plot on. If None, creates new figure
    """

    locations = _get_locations_for_montage(montage)
    _plot_electrode_montage(
        locations=locations,
        figsize=figsize, head_radius=head_radius,
        head_color=head_color, edge_color=edge_color,
        electrode_color=electrode_color, 
        fontsize=fontsize, ax=ax
    )

@enforce_type_hints
def plot_electrode_values(values: dict[str, float], montage: str = '10-10',
                          cmap: str = 'coolwarm', vmin: float | None = None, vmax: float | None = None,
                          head_radius: float | int = 1.0, figsize: tuple[int, int] = (8, 8),
                          head_color: str = 'white', edge_color='black',
                          hide_unused: bool = True,
                          fontsize: str | int = 'medium', ax: plt.Axes | None = None) -> None:
    """Plot electrode positions with color-coded values (topographic map).

    :param values: Dictionary mapping electrode names to values
    :param montage: EEG montage system ('10-10' or '10-20')
    :param cmap: Colormap for value visualization
    :param vmin: Minimum value for color scaling
    :param vmax: Maximum value for color scaling
    :param head_radius: Radius of the head outline
    :param figsize: Figure size as (width, height) in inches
    :param head_color: Fill color for the head outline
    :param edge_color: Color for head outline
    :param hide_unused: Whether to hide electrodes not in values dict
    :param fontsize: Font size for electrode labels
    :param ax: Matplotlib axes to plot on. If None, creates new figure
    """

    locations = _get_locations_for_montage(montage)
    if hide_unused:
        locations = {k: v for k, v in locations.items() if k in values.keys()}

    color_dict = _values_to_colors(values=values, cmap=cmap, vmin=vmin, vmax=vmax)

    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)

    _draw_head(ax, head_radius, head_color, edge_color)

    for name, location in locations.items():
        if name in values:
            _draw_electrode(ax, name, location, head_radius,
                            color_dict[name], edge_color, fontsize)

    ax.set_xlim((-head_radius * 1.25, head_radius * 1.25))
    ax.set_ylim((-head_radius * 1.25, head_radius * 1.25))
    ax.set_aspect('equal')
    ax.set_axis_off()



# -------- topography map plots


def plot_eeg_topography(recording: Recording, second: int | float,  # time moment
                        grid_resolution: int = 500, contour_levels: int = 20, colormap: str = 'RdBu_r',
                        add_contour_lines: bool = True, show_electrodes: bool = True,
                        figsize: tuple[int, int] = (8, 8), head_radius: float | int = 1.0,
                        head_color: str = "white", edge_color: str = "black", electrode_color: str = "black",
                        ax: plt.Axes | None = None) -> None:
    """Plot topographic map of EEG activity at a specific time moment.

    :param recording: Input EEG recording
    :param second: Time point to plot (in seconds)
    :param grid_resolution: Resolution of interpolation grid
    :param contour_levels: Number of contour levels for visualization
    :param colormap: Colormap for the topographic map
    :param add_contour_lines: Whether to add contour lines
    :param show_electrodes: Whether to show electrode positions
    :param figsize: Figure size as (width, height) in inches
    :param head_radius: Radius of the head outline
    :param head_color: Fill color for the head outline
    :param edge_color: Color for head outline
    :param electrode_color: Color for electrode markers
    :param ax: Matplotlib axes to plot on. If None, creates new figure
    """

    montage_name = _detect_montage_type(recording.channel_names)
    locations = _get_locations_for_montage(montage_name, recording.channel_names)

    sample_i = int(second * recording.sample_rate)
    values = {ch:v for ch, v in zip(recording.channel_names, recording.data[:, sample_i])}

    _plot_eeg_topography(locations=locations, values=values,
                         grid_resolution=grid_resolution, contour_levels=contour_levels, colormap=colormap,
                         add_contour_lines=add_contour_lines, show_electrodes=show_electrodes,
                         figsize=figsize, head_radius=head_radius,
                         head_color=head_color, edge_color=edge_color, electrode_color=electrode_color,
                         ax=ax, title=f"Topography map (time moment: {second} s)")

def plot_eeg_frequency_topography(recording: Recording, frequency: int,
                                  start_second: float, end_second: float,  # in seconds
                                  grid_resolution: int = 500, contour_levels: int = 20, colormap: str = 'RdBu_r',
                                  add_contour_lines: bool = True, show_electrodes: bool = True,
                                  figsize: tuple[int, int] = (8, 8), head_radius: float | int = 1.0,
                                  head_color: str = "white", edge_color: str = "black", electrode_color: str = "black",
                                  ax: plt.Axes | None = None) -> None:
    """Plot topographic map of power at a specific frequency.

    :param recording: Input EEG recording
    :param frequency: Target frequency for power calculation (in Hz)
    :param start_second: Start of time window for power calculation
    :param end_second: End of time window for power calculation
    :param grid_resolution: Resolution of interpolation grid
    :param contour_levels: Number of contour levels for visualization
    :param colormap: Colormap for the topographic map
    :param add_contour_lines: Whether to add contour lines
    :param show_electrodes: Whether to show electrode positions
    :param figsize: Figure size as (width, height) in inches
    :param head_radius: Radius of the head outline
    :param head_color: Fill color for the head outline
    :param edge_color: Color for head outline
    :param electrode_color: Color for electrode markers
    :param ax: Matplotlib axes to plot on. If None, creates new figure
    """

    montage_name = _detect_montage_type(recording.channel_names)
    locations = _get_locations_for_montage(montage_name, recording.channel_names)

    cut_recording = cut_by_second_range(recording, start_second, end_second)
    f, periodograms = get_frequency_spectrum(cut_recording)
    freq_i = np.searchsorted(f, frequency)
    values = {ch:v for ch, v in zip(recording.channel_names, periodograms[:, freq_i])}

    _plot_eeg_topography(locations=locations, values=values,
                         grid_resolution=grid_resolution, contour_levels=contour_levels, colormap=colormap,
                         add_contour_lines=add_contour_lines, show_electrodes=show_electrodes,
                         figsize=figsize, head_radius=head_radius,
                         head_color=head_color, edge_color=edge_color, electrode_color=electrode_color, 
                         ax=ax, title=f"Topography map: power of {frequency} Hz (time window: {start_second}-{end_second} s)")


# -------- ICA


def plot_ica_components(recording: Recording, n_components: int, duration: int = 10,
                        normal_range: float | int = 5.0, random_state: int = 42) -> None:
    """Plot Independent Component Analysis (ICA) components from EEG data.

    :param recording: Input EEG recording
    :param n_components: Number of ICA components to compute and display
    :param duration: Duration of signal segments to show around min/max values (in seconds)
    :param normal_range: Y-axis range for reference lines
    :param random_state: Random seed for reproducible ICA decomposition
    """

    components = get_ica_components(recording=recording, n_components=n_components, random_state=random_state)
    time = np.arange(0, recording.number_of_samples) / recording.sample_rate

    min_signal = np.abs(components).argmin(axis=1)
    max_signal = np.abs(components).argmax(axis=1)
    halflen = duration // 2 * recording.sample_rate    

    fig, ax = plt.subplots(n_components, 2, figsize=(14, n_components*1))
    for i in range(n_components):
        _plot_ica_component_segment(
            ax=ax[i, 0],
            time=time, component=components[i],
            sample=min_signal[i], halflen=halflen, normal_range=normal_range)
        _plot_ica_component_segment(
            ax=ax[i, 1],
            time=time, component=components[i],
            sample=max_signal[i], halflen=halflen, normal_range=normal_range)
        ax[i, 0].set_ylabel(f'IC {i}')        

    plt.suptitle('ICA sources')
    ax[0, 0].set_title("Around min source value")
    ax[0, 1].set_title("Around max source value")
        
    plt.tight_layout()
    plt.show()


def _plot_ica_component_segment(ax, time: np.ndarray, component: np.ndarray,
                                sample: int, halflen: int, normal_range: float) -> None:
    help_line_kwargs = {'alpha': 0.6, 'lw': 1, 'ls': '--', 'c': '#ff8800'}
    center_line_kwargs = {'alpha': 0.6, 'lw': 1, 'ls': '--', 'c': '#888888'}
    start, end = max(0, sample - halflen), min(sample + halflen, component.shape[-1])
    ax.plot(time[start:end], component[start:end], lw=1)
    ax.axhline(-normal_range, **help_line_kwargs)
    ax.axhline(normal_range, **help_line_kwargs)
    ax.axhline(0, **center_line_kwargs)
    ax.axvline(0, **help_line_kwargs)
    ax.axvline(time[-1], **help_line_kwargs)
    ax.set_xlim(time[start], time[end])
    ax.set_ylim(component[start:end].min(), component[start:end].max())


# -------- internal functions


def _plot_signal(data: np.ndarray, sample_rate: int | float, channel_names: list[str],
                 start: float | int = 0, duration: float | int = 5.0, center_data: bool = True,
                 cmap: str = 'Dark2', cmap_size: int = 8, padding: float | int = 1.0,
                 ax: plt.Axes | None = None) -> None:
    """Plot time-domain signal with channels spread vertically.

    :param data: EEG data of shape (channels, samples)
    :param sample_rate: Sampling rate in Hz
    :param channel_names: List of channel names
    :param start: From which second to start the plot
    :param duration: How many seconds to plot
    :param center_data: Whether to center each channel's data
    :param cmap: Colormap name to use
    :param cmap_size: Number of colors to use from colormap
    :param padding: Vertical spacing multiplier between channels
    :param ax: Matplotlib axes to plot on. If None, creates new figure
    """
    n_channels = len(channel_names)
    start_sample = int(start * sample_rate)
    n_samples = int(duration * sample_rate)
    time = np.arange(n_samples) / sample_rate + start

    visible_data = data[:, start_sample:n_samples+start_sample]
    offset = max([visible_data[i].std()*2 for i in range(n_channels)]) * padding

    color_cycle = _get_color_cycle(cmap=cmap, cmap_size=cmap_size)
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, n_channels/2 * padding))
    plt.box(False)

    yticks_positions = []
    for i in range(n_channels):
        to_plot = visible_data[i]
        if center_data:
            to_plot = to_plot - to_plot.mean() + i * offset
        ax.plot(time, to_plot, lw=1, alpha=0.8, color=next(color_cycle))
        yticks_positions.append(to_plot[0])

    ax.set_yticks(yticks_positions, channel_names)
    ax.set_ylabel('Channel name')
    ax.set_xlabel('Time (s)')
    ax.set_xlim(start, start+duration)
    ax.grid(True)


def _plot_electrode_montage(locations: dict[str, tuple[float, float]], electrode_names: list[str] | None = None,
                            hide_unused: bool = True, figsize: tuple[int, int] = (8, 8), head_radius: float | int = 1.0,
                            head_color: str = "white", edge_color: str = "black", electrode_color: str = "white",
                            electrode_highlight_color: str = "#fcb001", fontsize: str | int = "medium", ax: plt.Axes | None = None) -> None:
    if electrode_names:
        for name in electrode_names:
            if name not in locations.keys():
                print(f"Unrecognized electrode name: {name}, will be ignored")

    if hide_unused and electrode_names:
        locations = {k: v for k, v in locations.items() if k in electrode_names}

    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)

    _draw_head(ax, head_radius, head_color, edge_color)

    for name, location in locations.items():
        color = (electrode_highlight_color
                 if not hide_unused and electrode_names and name in electrode_names
                 else electrode_color)
        _draw_electrode(ax, name, location, head_radius, color, edge_color, fontsize)

    ax.set_xlim((-head_radius * 1.25, head_radius * 1.25))
    ax.set_ylim((-head_radius * 1.25, head_radius * 1.25))
    ax.set_aspect('equal')
    ax.set_axis_off()


def _draw_head(ax: plt.Axes, head_radius: float, head_color: str, edge_color: str) -> None:
    """Draw head outline with ears and nose.
    """
    import matplotlib.patches as patches

    ear_left = patches.Ellipse(
        xy=(-head_radius, 0),
        width=head_radius / 6,
        height=head_radius / 3,
        fill=True,
        facecolor=head_color,
        edgecolor=edge_color,
        lw=2
    )
    ear_right = patches.Ellipse(
        xy=(head_radius, 0),
        width=head_radius / 6,
        height=head_radius / 3,
        fill=True,
        facecolor=head_color,
        edgecolor=edge_color,
        lw=2
    )
    nose = patches.FancyArrow(
        x=0,
        y=head_radius * 0.95,
        dx=0,
        dy=head_radius / 5,
        fill=True,
        facecolor=head_color,
        edgecolor=edge_color,
        head_width=head_radius / 3,
        head_length=head_radius / 5,
        length_includes_head=True,
        lw=2
    )
    head_circle = patches.Circle(
        xy=(0, 0),
        radius=head_radius,
        facecolor=head_color,
        edgecolor=edge_color,
        fill=True,
        lw=2
    )
    inner_circle = patches.Circle(
        xy=(0, 0),
        radius=head_radius * 0.8,
        color=edge_color,
        fill=False,
        ls='--',
        lw=1
    )

    ax.add_patch(ear_left)
    ax.add_patch(ear_right)
    ax.add_patch(nose)
    ax.add_patch(head_circle)
    ax.add_patch(inner_circle)
    ax.plot([-head_radius, head_radius], [0, 0], ls='--', lw=1, color=edge_color)
    ax.plot([0, 0], [-head_radius, head_radius], ls='--', lw=1, color=edge_color)


def _draw_electrode(
        ax: plt.Axes,
        name: str,
        location: tuple[float, float],
        head_radius: float,
        color: str,
        edge_color: str,
        fontsize: str
) -> None:
    """Draw a single electrode circle with label.
    """
    import matplotlib.patches as patches

    electrode_circle = patches.Circle(
        xy=location,
        radius=head_radius / 14,
        facecolor=color,
        edgecolor=edge_color,
        fill=True,
        zorder=2
    )
    ax.add_patch(electrode_circle)

    ax.text(
        x=location[0],
        y=location[1],
        s=name,
        color=edge_color,
        va='center',
        ha='center',
        fontsize=fontsize,
        zorder=2
    )


def _interpolated_head_grid(coords_arr: np.ndarray, values_arr: np.ndarray, 
                            head_radius: float, grid_resolution: int):
    from scipy.interpolate import RBFInterpolator

    grid_extent = head_radius * 1.1  # Slightly larger than head
    xi = np.linspace(-grid_extent, grid_extent, grid_resolution)
    yi = np.linspace(-grid_extent, grid_extent, grid_resolution)
    xi_grid, yi_grid = np.meshgrid(xi, yi)
    
    rbf = RBFInterpolator(coords_arr, values_arr, kernel='thin_plate_spline')
    grid_points = np.column_stack([xi_grid.ravel(), yi_grid.ravel()])
    interpolated_values = rbf(grid_points).reshape(xi_grid.shape)

    # circular mask
    distance_from_center = np.sqrt(xi_grid**2 + yi_grid**2)
    circular_mask = distance_from_center <= head_radius
    masked_values = np.where(circular_mask, interpolated_values, np.nan)

    return xi_grid, yi_grid, masked_values


def _plot_eeg_topography(locations: dict[str, tuple[float, float]], values: dict[str, float],
                         grid_resolution: int = 500, contour_levels: int = 20, colormap: str = 'RdBu_r',
                         add_contour_lines: bool = True, contour_color: str = 'black', contour_alpha: float | int = 0.3,
                         show_electrodes: bool = False,
                         figsize: tuple[int, int] = (8, 8), head_radius: float | int = 1.0, electrode_size: float | int = 20.0,
                         head_color: str = "white", edge_color: str = "black", electrode_color: str = "black",
                         ax: plt.Axes | None = None, title: str = "") -> None:
    import matplotlib.patches as patches

    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)

    _draw_head(ax, head_radius, head_color, edge_color)

    ch_names = list(locations.keys())
    coords_arr = np.array([locations[ch] for ch in ch_names])
    values_arr = np.array([values[ch] for ch in ch_names])
    xi_grid, yi_grid, interpolated = _interpolated_head_grid(
        coords_arr=coords_arr, values_arr=values_arr, 
        head_radius=head_radius, grid_resolution=grid_resolution
    )
    contour_fill = ax.contourf(xi_grid, yi_grid, interpolated, 
                               levels=contour_levels, cmap=colormap, 
                               extend='both')
    if add_contour_lines:
        ax.contour(xi_grid, yi_grid, interpolated, 
                   levels=contour_levels//2, colors=contour_color, 
                   alpha=contour_alpha, linewidths=0.5)

    if show_electrodes:
        ax.scatter(coords_arr[:, 0], coords_arr[:, 1], c=electrode_color, s=electrode_size, zorder=5)
    head_circle = patches.Circle(xy=(0, 0), radius=head_radius, color=edge_color, fill=False, lw=2)
    ax.add_patch(head_circle)

    ax.set_xlim((-head_radius * 1.25, head_radius * 1.25))
    ax.set_ylim((-head_radius * 1.25, head_radius * 1.25))
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_title(title)

    cbar = plt.colorbar(contour_fill, ax=ax, shrink=0.8, aspect=20)
    cbar.set_label('Amplitude', rotation=270, labelpad=15)


# ---- helping functions


def _get_color_cycle(cmap: str = 'Dark2', cmap_size: int = 8):
    from matplotlib import colormaps
    from itertools import cycle
    return cycle(colormaps[cmap](np.linspace(0, 1, cmap_size)))


def _values_to_colors(values: dict[str, float], cmap: str, vmin: float, vmax: float) -> dict:
    import matplotlib.colors as colors
    from matplotlib import colormaps
    vmin = vmin or min(values.values())
    vmax = vmax or min(values.values())
    norm = colors.Normalize(vmin=vmin, vmax=vmax)
    colormap = colormaps.get_cmap(cmap)
    color_dict = {name: colormap(norm(values[name])) for name in values}
    return color_dict


def _get_locations_for_montage(montage_name: str = "10-10", channel_names: list[str] | None = None) -> dict[str, tuple[float, float]]:
    if montage_name in ['10-20', '10_20', '1020']:
        locations = EEG_MONTAGES['10-20']
    elif montage_name in ['10-10', '10_10', '1010']:
        locations = EEG_MONTAGES['10-10']
    else:
        raise BreesyError(f'Unknown montage type: {montage_name}. Use either 10-10 (default) or 10-20.')
    if channel_names is not None:
        locations = {ch: coords for ch, coords in locations.items() if ch in channel_names}
        if len(locations) < len(channel_names):
            unknown_channels = [ch for ch in channel_names if ch not in locations.keys()]
            raise BreesyError(f'Found unknown channel(s) not defined for the {montage_name} montage: {", ".join(unknown_channels)}')
    return locations


def _detect_montage_type(ch_names: list[str]) -> str:
    if any([ch.lower() in [x.lower() for x in EEG_MONTAGES['10-10'].keys()] for ch in ch_names]):
        print("Using 10-10 montage...")
        return "10-10"
    else:
        print("Using 10-20 montage...")
        return "10-20"
