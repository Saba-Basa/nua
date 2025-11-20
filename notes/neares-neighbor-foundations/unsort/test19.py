import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

def plot_bands(points, ax):
    ax.clear()
    ax.scatter(points[:,0], points[:,1], c='black', zorder=10)
    rect = plt.Rectangle((-5, -5), 10, 10, linewidth=2, edgecolor='black', facecolor='none', zorder=1)
    ax.add_patch(rect)

    xvals = points[:,0]
    yvals = points[:,1]

    x_edges = np.percentile(xvals, [0, 33, 66, 100])
    y_edges = np.percentile(yvals, [0, 33, 66, 100])
    band_colors = ['red', 'blue', 'green']
    alpha_val = 0.15

    for i in range(len(x_edges)-1):
        ax.axvspan(x_edges[i], x_edges[i+1], color=band_colors[i], alpha=alpha_val, zorder=2)
    for i in range(len(y_edges)-1):
        ax.axhspan(y_edges[i], y_edges[i+1], color=band_colors[i], alpha=alpha_val, zorder=2)
    mini_rect = plt.Rectangle((x_edges[1], y_edges[1]),
                              x_edges[2]-x_edges[1], y_edges[2]-y_edges[1],
                              linewidth=2, edgecolor='gray', facecolor='none', zorder=5)
    ax.add_patch(mini_rect)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.axis('off')
    plt.draw()

# Initial points
np.random.seed(0)
points = np.random.uniform(-5, 5, (18, 2))

fig, ax = plt.subplots(figsize=(5, 5))
plot_bands(points, ax)

# Add button
ax_button = plt.axes([0.85, 0.02, 0.13, 0.05])  # [left, bottom, width, height]
button = Button(ax_button, 'Regenerate Points')

def on_button_clicked(event):
    new_points = np.random.uniform(-5, 5, (18, 2))
    plot_bands(new_points, ax)

button.on_clicked(on_button_clicked)
plt.show()
