"""Example of using Breesy's electrode location plotting functions."""

import matplotlib.pyplot as plt

from breesy.plots import plot_electrode_montage_10_20, plot_electrode_values, plot_electrode_montage_10_10

# Example 1: Plot all 10-20 system electrodes
print("Plotting all 10-20 electrodes...")
plot_electrode_montage_10_20()

# Example 2: Highlight specific electrodes
print("\nHighlighting motor cortex electrodes...")
motor_electrodes = ['C3', 'Cz', 'C4', 'FC3', 'FCz', 'FC4']
plot_electrode_montage_10_20(
    electrode_names=motor_electrodes,
    electrode_highlight_color='red',
    hide_unused=False  # Show all electrodes but highlight selected ones
)

# Example 3: Show only selected electrodes from 10-10 system
print("\nShowing only frontal electrodes from 10-10 system...")
frontal_electrodes = ['Fp1', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8',
                      'AF7', 'AF3', 'AFz', 'AF4', 'AF8']
plot_electrode_montage_10_10(
    electrode_names=frontal_electrodes,
    electrode_color='lightblue',
    hide_unused=True
)

# Example 4: Plot with custom colors and in subplots
print("\nCreating subplot with both montages...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

plot_electrode_montage_10_20(
    ax=ax1,
    head_color='lightblue',
    fontsize='small'
)
ax1.set_title('10-20 System')

plot_electrode_montage_10_10(
    ax=ax2,
    head_color='lightpink',
    fontsize='small'
)
ax2.set_title('10-10 System')

plt.tight_layout()
plt.show()

# Example 5: Plot electrode values (topographic map)
print("\nPlotting topographic map...")

# Simulate some alpha power values
alpha_values = {
    'O1': 0.9, 'O2': 0.85, 'Oz': 0.88,
    'P3': 0.7, 'P4': 0.68, 'Pz': 0.72,
    'C3': 0.5, 'C4': 0.48, 'Cz': 0.52,
    'F3': 0.3, 'F4': 0.28, 'Fz': 0.32
}

plot_electrode_values(
    values=alpha_values,
    montage='10-20',
    cmap='hot',
    vmin=0,
    vmax=1
)
plt.title('Alpha Power Distribution')
plt.show()

# Example 6: Multiple topographic maps
print("\nComparing conditions with topographic maps...")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Simulate data for three conditions
conditions = {
    'Rest': {'Fz': 0.3, 'Cz': 0.4, 'Pz': 0.8, 'Oz': 0.9},
    'Task': {'Fz': 0.7, 'Cz': 0.6, 'Pz': 0.5, 'Oz': 0.4},
    'Recovery': {'Fz': 0.4, 'Cz': 0.5, 'Pz': 0.7, 'Oz': 0.8}
}

for ax, (condition, values) in zip(axes, conditions.items()):
    plot_electrode_values(
        values=values,
        montage='10-20',
        cmap='viridis',
        vmin=0,
        vmax=1,
        ax=ax
    )
    ax.set_title(condition)

plt.tight_layout()
plt.show()
