import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

np.random.seed(0)
N_POINTS = 18
points = np.random.uniform(-5, 5, (N_POINTS, 2))

def plot_adaptive_yellow(points):
    ax.clear()
    ax.scatter(points[:,0], points[:,1], c='black', zorder=10)
    ax.add_patch(plt.Rectangle((-5, -5), 10, 10, linewidth=2,
                               edgecolor='black', facecolor='none', zorder=1))

    # Use 40% quantile for a larger overlap region
    x_edge = np.percentile(points[:,0], 40)
    y_edge = np.percentile(points[:,1], 60)

    # Draw adaptive yellow region: left of x_edge, above y_edge
    ax.add_patch(plt.Rectangle(
        (-5, y_edge), x_edge + 5, 5 - y_edge,
        color='yellow', alpha=0.25, zorder=2))

    # Highlight points inside yellow region
    yellow_points = np.array([pt for pt in points if pt[0] <= x_edge and pt[1] >= y_edge])
    if len(yellow_points):
        ax.scatter(yellow_points[:,0], yellow_points[:,1], c='orange', s=80, marker='o',
                   edgecolor='red', zorder=11, label='Adaptive points in yellow')

    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.axis('off')
    ax.legend()
    plt.draw()

fig, ax = plt.subplots(figsize=(5, 5))
plot_adaptive_yellow(points)

ax_button = plt.axes([0.85, 0.02, 0.13, 0.05])
button = Button(ax_button, 'Regenerate Points')
def on_button_clicked(event):
    new_points = np.random.uniform(-5, 5, (N_POINTS, 2))
    plot_adaptive_yellow(new_points)
button.on_clicked(on_button_clicked)
plt.show()
