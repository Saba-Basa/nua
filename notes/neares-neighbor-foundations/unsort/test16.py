import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Torus parameters (same as your code)
R = 3  # Major radius
r = 1  # Minor radius
n_points = 1000  # Sample as point cloud (X)

# Sample point cloud X from torus (discrete points on manifold)
u = np.random.uniform(0, 2*np.pi, n_points)
v = np.random.uniform(0, 2*np.pi, n_points)
X = np.zeros((n_points, 3))  # X: (n_points, 3)
X[:, 0] = (R + r * np.cos(v)) * np.cos(u)  # x
X[:, 1] = (R + r * np.cos(v)) * np.sin(u)  # y
X[:, 2] = r * np.sin(v)  # z (use as filter, like height)

# Filter and Cover (simple: f = z-height; overlapping intervals like chart domains)
def filter_and_cover_points(X, filter_col=2, n_intervals=4, overlap_frac=0.3):
    filter_values = X[:, filter_col]  # f: X -> R (z as 'v' param)
    f_min, f_max = filter_values.min(), filter_values.max()
    range_len = f_max - f_min
    interval_len = range_len / (n_intervals - overlap_frac * (n_intervals - 1))
    starts = np.linspace(f_min, f_max - interval_len, n_intervals)
    cover = [(start, start + interval_len) for start in starts]  # Overlapping I_i like [u_min, u_max]
    
    pullbacks = []  # T = {U_i}: list of point indices in each I_i
    colors = ['cyan', 'yellow', 'green', 'magenta']  # Like your chart colors
    for i, (start, end) in enumerate(cover):
        mask = (filter_values >= start) & (filter_values <= end)
        indices = np.where(mask)[0]
        if len(indices) > 0:
            pullbacks.append((indices, colors[i % len(colors)]))  # U_i ⊆ X, colored
    return pullbacks, cover  # T's open subsets via pullbacks

# Get pullbacks (charts on cloud)
pullbacks, cover = filter_and_cover_points(X, n_intervals=3)  # 3 charts like U_i, U_j, overlap

# Plot: 3D point cloud with overlapping colored patches (like your left subplot)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c='lightgray', alpha=0.2, s=10, label='Full X (torus cloud)')  # Base cloud

colors_used = {}  # Track for overlaps (multi-color points)
for idx, (indices, color) in enumerate(pullbacks):
    points_in_Ui = X[indices]
    # For overlaps: points in multiple U_i get blended (e.g., green-cyan)
    for pt_idx in indices:
        if pt_idx in colors_used:
            colors_used[pt_idx] = 'green'  # Overlap color (like U_i ∩ U_j)
        else:
            colors_used[pt_idx] = color
    ax.scatter(points_in_Ui[:, 0], points_in_Ui[:, 1], points_in_Ui[:, 2], 
               c=color, alpha=0.6, s=20, label=f'U_{idx} (pullback)')  # Colored patches

ax.set_title('Point Cloud X with Filter/Cover Patches\n(Like Torus Charts: Overlaps in Green)', fontsize=12)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z (filter)')
ax.legend(); plt.show()

# Optional: Plot filter line with cover intervals (like your middle subplot)
fig2, ax2 = plt.subplots()
filter_values = X[:, 2]
ax2.scatter(range(len(filter_values)), filter_values, alpha=0.5, s=1)  # Points on filter line
for i, (start, end) in enumerate(cover):
    ax2.axvspan(0, len(filter_values), ymin=start, ymax=end, alpha=0.3, 
                color=pullbacks[i][1], label=f'I_{i}')
ax2.set_title('Filter f(X) = z with Overlapping Cover (Parameter Space)')
ax2.set_xlabel('Point Index'); ax2.set_ylabel('z-height')
ax2.legend(); plt.show()
