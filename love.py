import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Create figure with 1x4 subplots
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

# Compute data for each plot
x_L = np.linspace(0.1, 5, 1000)
y_L = 1 / x_L

theta = np.linspace(0, 2 * np.pi, 1000)
radius = 3
x_O = radius * np.cos(theta)
y_O = radius * np.sin(theta)

x_V = np.linspace(-2, 3, 1000)
y_V = np.abs(1 - 2 * x_V)

y_E = np.linspace(-3, 3, 1000)
x_E = -3 * np.abs(np.sin(y_E))

# Set up each subplot with limits, titles, and grids
# L: y = 1/x
axes[0].set_xlim(0, 5)
axes[0].set_ylim(0, 5)
axes[0].set_title("y = 1/x", color='r')
axes[0].grid(True, linestyle='--', alpha=0.7)

# O: x²+y²=9
axes[1].set_xlim(-4, 4)
axes[1].set_ylim(-4, 4)
axes[1].set_title("x²+y²=9", color='r')
axes[1].grid(True, linestyle='--', alpha=0.7)

# V: y = |1-2x|
axes[2].set_xlim(-2, 3)
axes[2].set_ylim(-1, 5)
axes[2].set_title("y = |1-2x|", color='r')
axes[2].grid(True, linestyle='--', alpha=0.7)

# E: x = -3|sin(y)|
axes[3].set_xlim(-5, 2.5)
axes[3].set_ylim(-4.5, 4.5)
axes[3].set_title("x = -3|sin(y)|", color='r')
axes[3].grid(True, linestyle='--', alpha=0.7)

# Ensure all plots have equal aspect ratio
for ax in axes:
    ax.set_aspect('equal')

# Create line objects with empty data
line_L, = axes[0].plot([], [], 'r', linewidth=3)
line_O, = axes[1].plot([], [], 'r', linewidth=3)
line_V, = axes[2].plot([], [], 'r', linewidth=3)
line_E, = axes[3].plot([], [], 'r', linewidth=3)

# Define the update function for animation
def update(i):
    # Update each line with data up to frame i+1
    line_L.set_data(x_L[:i+1], y_L[:i+1])
    line_O.set_data(x_O[:i+1], y_O[:i+1])
    line_V.set_data(x_V[:i+1], y_V[:i+1])
    line_E.set_data(x_E[:i+1], y_E[:i+1])
    return line_L, line_O, line_V, line_E

# Create the animation
N_frames = 1000  # Matches the number of data points for smooth drawing
anim = animation.FuncAnimation(fig, update, frames=N_frames, interval=10, blit=True)

# Adjust layout and add suptitle
plt.tight_layout()
plt.suptitle("Equations of Life", fontsize=16, y=1.05)

# Display the animation
plt.show()