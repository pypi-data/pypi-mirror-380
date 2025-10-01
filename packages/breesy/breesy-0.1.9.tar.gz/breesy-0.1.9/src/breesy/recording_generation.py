import os
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

from .errors import BreesyError
from .signal_generation import (
    generate_background_activity,
    generate_mu_effect,
    generate_cognitive_load_effect,
    generate_working_memory_effect,
    concatenate_eeg_trials, generate_band_activity, generate_spindle
)
from .type_hints import enforce_type_hints


@enforce_type_hints
def generate_motor_imagery_dataset(
        n_subjects: int,
        sample_rate: int | float,
        powerline_freq: int,  # TODO: do we use these params
        powerline_strength: float | int,
        channel_names: list[str],
        n_trials_per_class: int,
        trial_duration: float | int,
        output_dir: str,
        mu_strength: float | int = 1.0,
        random_state: int = 42,
        generate_metadata: bool = True
) -> None:
    """Generate a motor imagery EEG dataset.

    :param n_subjects: Number of subjects to generate data for
    :param sample_rate: Sampling rate in Hz
    :param powerline_freq: Frequency of powerline noise (50 or 60 Hz)
    :param powerline_strength: Amplitude of powerline noise
    :param channel_names: List of EEG channel names
    :param n_trials_per_class: Number of trials per class (left/right)
    :param trial_duration: Duration of each trial in seconds
    :param output_dir: Directory to save the dataset
    :param mu_strength: Strength of mu rhythm modulation
    :param random_state: Random seed for reproducibility
    :param generate_metadata: Whether to generate metadata files
    """
    class_labels = ['left', 'right']
    n_classes = len(class_labels)

    rng = np.random.default_rng(random_state)
    os.makedirs(output_dir, exist_ok=True)
    metadata = []

    for subject in range(n_subjects):
        subject_id = f'sub-{subject + 1:03d}'

        # Initialize arrays
        n_total_trials = n_classes * n_trials_per_class
        trial_samples = int(trial_duration * sample_rate)

        # Generate balanced trial labels
        trial_labels = []
        for c in range(n_classes):
            trial_labels.extend([class_labels[c]] * n_trials_per_class)
        rng.shuffle(trial_labels)

        X, trial_info = [], []

        # Generate trials
        for trial_idx in range(n_total_trials):
            label = trial_labels[trial_idx]

            # Generate background activity
            trial_data = generate_background_activity(
                sample_rate,
                trial_samples,
                channel_names,
                random_state=random_state + trial_idx
            )

            # Add mu rhythm modulation
            mu_effect = generate_mu_effect(
                sample_rate,
                trial_samples,
                channel_names,
                side=label,
                strength=mu_strength
            )
            trial_data += mu_effect

            # Store trial data and metadata
            X.append(trial_data)
            trial_info.append({
                'subject_id': subject_id,
                'trial_number': trial_idx + 1,
                'class': label,
                'duration': trial_duration
            })

        X = np.array(X)  # Shape: (n_trials, n_channels, n_samples)

        # Save data and metadata
        subject_dir = os.path.join(output_dir, subject_id)
        os.makedirs(subject_dir, exist_ok=True)
        np.save(os.path.join(subject_dir, 'eeg_data.npy'), X)

        if generate_metadata:
            subject_metadata = pd.DataFrame(trial_info)
            subject_metadata.to_csv(os.path.join(subject_dir, 'metadata.csv'), index=False)
            metadata.extend(trial_info)

    if generate_metadata:
        complete_metadata = pd.DataFrame(metadata)
        complete_metadata.to_csv(os.path.join(output_dir, 'dataset_metadata.csv'), index=False)

        description = {
            'sampling_rate': sample_rate,
            'channels': channel_names,
            'n_subjects': n_subjects,
            'n_trials_per_class': n_trials_per_class,
            'trial_duration': trial_duration
        }
        pd.DataFrame([description]).to_json(
            os.path.join(output_dir, 'dataset_description.json'),
            orient='records'
        )


@enforce_type_hints
def generate_cognitive_load_dataset(
        n_subjects: int,
        sample_rate: int | float,
        powerline_freq: int,  # TODO: do we want to use these params
        powerline_strength: float,
        channel_names: list[str],
        n_trials_per_class: int,
        trial_duration: float | int,
        iti_range: tuple[float, float],
        output_dir: str,
        random_state: int = 42,
        generate_metadata: bool = True
) -> None:
    """Generate a cognitive load EEG dataset.

    :param n_subjects: Number of subjects to generate data for
    :param sample_rate: Sampling rate in Hz
    :param powerline_freq: Frequency of powerline noise (50 or 60 Hz)
    :param powerline_strength: Amplitude of powerline noise
    :param channel_names: List of EEG channel names
    :param n_trials_per_class: Number of trials per condition
    :param trial_duration: Duration of each trial in seconds
    :param iti_range: Tuple of (min_iti, max_iti) in seconds
    :param output_dir: Directory to save the dataset
    :param random_state: Random seed for reproducibility
    :param generate_metadata: Whether to generate metadata files
    """
    class_labels = ['rest', 'easy', 'medium', 'hard']
    n_classes = len(class_labels)

    rng = np.random.default_rng(random_state)
    os.makedirs(output_dir, exist_ok=True)
    metadata = []

    for subject in range(n_subjects):
        subject_id = f'subj-{subject + 1:03d}'

        # Initialize arrays
        n_total_trials = n_classes * n_trials_per_class
        trial_samples = int(trial_duration * sample_rate)

        # Generate balanced trial labels
        trial_labels = []
        for c in range(n_classes):
            trial_labels.extend([class_labels[c]] * n_trials_per_class)
        rng.shuffle(trial_labels)

        X, trial_info = [], []

        # Generate trials
        for trial_idx in range(n_total_trials):
            label = trial_labels[trial_idx]

            # Generate base activity
            trial_data = generate_background_activity(
                sample_rate,
                trial_samples,
                channel_names,
                random_state=random_state + trial_idx
            )

            # Add cognitive load effects
            cognitive_effect = generate_cognitive_load_effect(
                condition=label,
                sample_rate=sample_rate,
                n_samples=trial_samples,
                channel_names=channel_names,
                random_state=random_state + trial_idx * 2
            )
            trial_data += cognitive_effect

            # Add working memory effects
            memory_effect = generate_working_memory_effect(
                condition=label,
                sample_rate=sample_rate,
                n_samples=trial_samples,
                channel_names=channel_names,
                random_state=random_state + trial_idx * 3
            )
            trial_data += memory_effect

            # Store trial data and metadata
            X.append(trial_data)
            trial_info.append({
                'subject_id': subject_id,
                'trial_number': trial_idx + 1,
                'class': label,
                'duration': trial_duration
            })

        X = np.array(X)
        subject_metadata = pd.DataFrame(trial_info)

        # Concatenate trials with ITIs
        continuous_data, continuous_metadata = concatenate_eeg_trials(
            trials=X,
            sample_rate=sample_rate,
            channel_names=channel_names,
            trial_info=subject_metadata.to_dict('records'),
            iti_range=iti_range,
            random_state=random_state + 101
        )

        # Save data and metadata
        subject_dir = os.path.join(output_dir, subject_id)
        os.makedirs(subject_dir, exist_ok=True)
        np.save(os.path.join(subject_dir, 'eeg_data.npy'), continuous_data)
        continuous_metadata.to_csv(os.path.join(subject_dir, 'metadata.csv'), index=False)
        metadata.extend(trial_info)

    if generate_metadata:
        complete_metadata = pd.DataFrame(metadata)
        complete_metadata.to_csv(os.path.join(output_dir, 'dataset_metadata.csv'), index=False)

        description = {
            'sampling_rate': sample_rate,
            'channels': channel_names,
            'n_subjects': n_subjects,
            'n_trials_per_class': n_trials_per_class,
            'trial_duration': trial_duration,
            'iti_range': iti_range
        }
        pd.DataFrame([description]).to_json(
            os.path.join(output_dir, 'dataset_description.json'),
            orient='records'
        )


@enforce_type_hints
def generate_sleep_stage(
        stage: str,
        sample_rate: int | float,
        n_samples: int,
        channel_names: list[str],
        random_state: int = 42,
) -> np.ndarray:
    """Generate EEG data for a specific sleep stage.

    :param stage: Sleep stage ('Wake', 'N1', 'N2', 'N3', or 'REM')
    :param sample_rate: Sampling rate in Hz
    :param n_samples: Number of samples to generate
    :param channel_names: List of EEG channel names
    :param random_state: Random seed for reproducibility

    :return: 2D numpy array of shape (n_channels, n_samples)
    """
    valid_stages = ['Wake', 'N1', 'N2', 'N3', 'REM']
    if stage not in valid_stages:
        raise BreesyError(
            f"Invalid sleep stage: {stage}",
            f"Stage must be one of: {', '.join(valid_stages)}"
        )

    rng = np.random.default_rng(random_state)
    n_channels = len(channel_names)

    # Generate base activity
    data = generate_background_activity(
        sample_rate,
        n_samples,
        channel_names,
        random_state=random_state
    )

    # Add stage-specific features
    duration = n_samples / sample_rate

    if stage == 'Wake':
        # Strong alpha in posterior channels
        alpha = generate_band_activity(
            n_samples,
            sample_rate,
            8, 13,
            random_state=random_state * 2
        )
        for ch in range(n_channels):
            if any(name in channel_names[ch] for name in ['O', 'P']):
                data[ch] += 2 * alpha

    elif stage == 'N1':
        # Theta activity and vertex sharp waves
        theta = generate_band_activity(
            n_samples,
            sample_rate,
            4, 8,
            random_state=random_state * 3
        )
        for ch in range(n_channels):
            if 'C' in channel_names[ch]:
                data[ch] += 1.5 * theta

    elif stage == 'N2':
        # Sleep spindles and K-complexes
        n_spindles = rng.poisson(duration / 3)  # ~1 spindle per 3s
        for _ in range(n_spindles):
            spindle_start = rng.integers(0, n_samples - int(0.5 * sample_rate))
            spindle = generate_spindle(
                sample_rate,
                int(0.5 * sample_rate),
                random_state=random_state * 4
            )
            for ch in range(n_channels):
                if any(name in channel_names[ch] for name in ['C', 'F']):
                    data[ch, spindle_start:spindle_start + len(spindle)] += spindle

    elif stage == 'N3':
        # High-amplitude slow waves
        delta = generate_band_activity(
            n_samples,
            sample_rate,
            0.5, 2,
            random_state=random_state * 5
        )
        for ch in range(n_channels):
            if any(name in channel_names[ch] for name in ['F', 'C']):
                data[ch] += 3 * delta

    elif stage == 'REM':
        # Mixed frequency low amplitude activity
        mixed = generate_band_activity(
            n_samples,
            sample_rate,
            4, 8,
            random_state=random_state * 6
        )
        for ch in range(n_channels):
            if any(name in channel_names[ch] for name in ['C', 'F']):
                data[ch] += 0.5 * mixed

    return data


@enforce_type_hints
def generate_sleep_stages_sequence(
        n_epochs: int,
        random_state: int = 42,
) -> list[str]:
    """Generate a realistic sequence of sleep stages using a Markov chain.

    :param n_epochs: Number of epochs to generate
    :param random_state: Random seed for reproducibility

    :return: List of sleep stage labels
    """
    stage_names = ['Wake', 'N1', 'N2', 'N3', 'REM']

    # Transition probabilities matrix
    transition_matrix = np.array([
        [0.80, 0.15, 0.05, 0.00, 0.00],  # Wake →
        [0.10, 0.70, 0.15, 0.00, 0.05],  # N1 →
        [0.05, 0.10, 0.70, 0.10, 0.05],  # N2 →
        [0.00, 0.00, 0.15, 0.80, 0.05],  # N3 →
        [0.05, 0.10, 0.10, 0.00, 0.75]  # REM →
    ])

    rng = np.random.default_rng(random_state)
    stages = np.zeros(n_epochs, dtype=int)

    # Start with Wake
    stages[0] = 0

    # Generate sequence using transition probabilities
    for i in range(1, n_epochs):
        stages[i] = rng.choice(len(stage_names), p=transition_matrix[stages[i - 1]])

    return [stage_names[s] for s in stages]


@enforce_type_hints
def generate_sleep_dataset(
        n_subjects: int,
        sample_rate: int | float,
        powerline_freq: int,  # TODO: do we want to use these parameters
        powerline_strength: float,
        channel_names: list[str],
        record_duration: float | int,
        epoch_duration: float | int,
        output_dir: str,
        random_state: int = 42,
        generate_metadata: bool = True
) -> None:
    """Generate a sleep EEG dataset.

    :param n_subjects: Number of subjects to generate data for
    :param sample_rate: Sampling rate in Hz
    :param powerline_freq: Frequency of powerline noise (50 or 60 Hz)
    :param powerline_strength: Amplitude of powerline noise
    :param channel_names: List of EEG channel names
    :param record_duration: Total duration of recording in seconds
    :param epoch_duration: Duration of each epoch in seconds
    :param output_dir: Directory to save the dataset
    :param random_state: Random seed for reproducibility
    :param generate_metadata: Whether to generate metadata files
    """
    rng = np.random.default_rng(random_state)
    os.makedirs(output_dir, exist_ok=True)
    metadata = []

    for subject in range(n_subjects):
        subject_id = f'subj-{subject + 1:03d}'

        # Calculate number of epochs
        n_epochs = int(record_duration // epoch_duration)
        epoch_samples = int(epoch_duration * sample_rate)

        # Generate sleep stage sequence
        sleep_stages = generate_sleep_stages_sequence(n_epochs, random_state + subject)

        epochs, epoch_info = [], []

        # Generate data for each epoch
        for epoch_idx, stage in enumerate(sleep_stages):
            epoch_data = generate_sleep_stage(
                stage,
                sample_rate,
                epoch_samples,
                channel_names,
                random_state=random_state + rng.integers(1, 100)
            )
            epochs.append(epoch_data)

            # Generate timing information
            recording_start = datetime(2024, 1, 1, 22, 0)  # Start at 22:00
            epoch_start = recording_start + timedelta(seconds=epoch_idx * epoch_duration)

            epoch_info.append({
                'subject_id': subject_id,
                'epoch_number': epoch_idx + 1,
                'stage': stage,
                'start_time': epoch_start.strftime('%H:%M:%S'),
                'duration': epoch_duration
            })

        # Concatenate all epochs
        full_recording = np.hstack(epochs)

        # Save data and metadata
        subject_dir = os.path.join(output_dir, subject_id)
        os.makedirs(subject_dir, exist_ok=True)
        np.save(os.path.join(subject_dir, 'eeg_data.npy'), full_recording)

        if generate_metadata:
            subject_metadata = pd.DataFrame(epoch_info)
            subject_metadata.to_csv(os.path.join(subject_dir, 'metadata.csv'), index=False)
            metadata.extend(epoch_info)

    if generate_metadata:
        complete_metadata = pd.DataFrame(metadata)
        complete_metadata.to_csv(os.path.join(output_dir, 'dataset_metadata.csv'), index=False)

        description = {
            'sampling_rate': sample_rate,
            'channels': channel_names,
            'n_subjects': n_subjects,
            'record_duration': record_duration,
            'epoch_duration': epoch_duration
        }
        pd.DataFrame([description]).to_json(
            os.path.join(output_dir, 'dataset_description.json'),
            orient='records'
        )


if __name__ == "__main__":
    # Example usage: Generate a small motor imagery dataset
    generate_motor_imagery_dataset(
        n_subjects=2,
        sample_rate=250,
        powerline_freq=50,
        powerline_strength=0.1,
        channel_names=['F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2'],
        n_trials_per_class=10,
        trial_duration=3.0,
        output_dir='example_motor_imagery',
        mu_strength=1.0,
        random_state=42
    )

    # Example usage: Generate a small cognitive load dataset
    generate_cognitive_load_dataset(
        n_subjects=2,
        sample_rate=1000,
        powerline_freq=50,
        powerline_strength=0.1,
        channel_names=['Fz', 'Cz', 'Pz', 'Oz'],
        n_trials_per_class=5,
        trial_duration=10.0,
        iti_range=(2.0, 3.0),
        output_dir='example_cognitive_load',
        random_state=42
    )

    # Example usage: Generate a small sleep dataset
    generate_sleep_dataset(
        n_subjects=1,
        sample_rate=500,
        powerline_freq=50,
        powerline_strength=0.1,
        channel_names=['F3', 'F4', 'C3', 'C4', 'O1', 'O2'],
        record_duration=1800,  # 30 minutes
        epoch_duration=30.0,
        output_dir='example_sleep',
        random_state=42
    )
