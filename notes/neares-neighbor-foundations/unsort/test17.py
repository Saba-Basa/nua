import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Torus params (R major, r minor radius)
R, r = 3, 1
n_points = 2000  # Denser cloud for manifold approx (X)

# Sample point cloud X: Discrete points on torus manifold
theta = np.random.uniform(0, 2*np.pi, n_points)  # u: major angle
phi = np.random.uniform(0, 2*np.pi, n_points)    # v: minor angle
X = np.column_stack([
    (R + r * np.cos(phi)) * np.cos(theta),  # x
    (R + r * np.cos(phi)) * np.sin(theta),  # y
    r * np.sin(phi)                         # z (height filter f)
])  # X: (n_points, 3) — finite set, approx infinite manifold

# Filter f = z-height (projects to 1D line, like manifold coord)
z_values = X[:, 2]  # f: X → R
z_min, z_max = z_values.min(), z_values.max()

# Cover: Overlapping intervals on f(X) (pullbacks U_i ⊆ X)
n_intervals, overlap_frac = 5, 0.3
range_len = z_max - z_min
interval_len = range_len / (n_intervals - overlap_frac * (n_intervals - 1))
starts = np.linspace(z_min, z_max - interval_len, n_intervals)
cover = [(start, start + interval_len) for start in starts]

pullbacks = []  # T = {U_i}: subsets (indices where z in interval)
colors = plt.cm.viridis(np.linspace(0, 1, n_intervals))  # Gradient like your alien graph
overlap_points = set()  # Track for green overlaps (finite intersections closed)

for i, (z_start, z_end) in enumerate(cover):
    mask = (z_values >= z_start) & (z_values <= z_end)
    indices = np.where(mask)[0]
    if len(indices) == 0:
        print(f"Empty pullback U_{i} (∅ ⊆ X vacuously true, skip)")  # Ties to Q8
        continue
    pullbacks.append((indices, colors[i]))  # U_i open by declaration in T
    overlap_points.update(indices)  # Simple overlap detect (shared pts)

# Plot: 3D cloud with height-colored pullbacks (manifold patches)
fig = plt.figure(figsize=(12, 5))

# Left: Full cloud colored by height (f(X)), like alien skeleton base
ax1 = fig.add_subplot(121, projection='3d')
scatter = ax1.scatter(X[:, 0], X[:, 1], X[:, 2], c=z_values, cmap='viridis', alpha=0.6, s=10)
ax1.set_title('Torus Point Cloud X\nColored by Height Filter f(z) (Many Manifolds Possible)')
ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('z-height')
plt.colorbar(scatter, ax=ax1, label='f(z) Gradient (Blue Low, Yellow High)')

# Right: Pullbacks as colored subsets (U_i on manifold, overlaps blended)
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(X[:, 0], X[:, 1], X[:, 2], c='lightgray', alpha=0.2, s=5, label='Full X')  # Base
for i, (indices, color) in enumerate(pullbacks):
    pts_Ui = X[indices]
    overlap_mask = np.isin(indices, list(overlap_points - set(indices)))  # Shared pts
    if np.any(overlap_mask):
        ax2.scatter(pts_Ui[overlap_mask, 0], pts_Ui[overlap_mask, 1], pts_Ui[overlap_mask, 2],
                    c='green', alpha=0.8, s=15, label=f'Overlap U_i ∩ U_j' if i==0 else "")
    ax2.scatter(pts_Ui[~overlap_mask, 0], pts_Ui[~overlap_mask, 1], pts_Ui[~overlap_mask, 2],
                c=color, alpha=0.7, s=20, label=f'U_{i} Pullback')
ax2.set_title('Cover Pullbacks on Torus Cloud\n(Overlaps Green, Like Manifold Charts)')
ax2.set_xlabel('x'); ax2.set_ylabel('y'); ax2.set_zlabel('z-height')
ax2.legend()

# Filter line with cover (1D param space)
fig3, ax3 = plt.subplots(figsize=(8, 2))
ax3.scatter(range(n_points), z_values, c=z_values, cmap='viridis', s=1, alpha=0.5)
for i, (z_start, z_end) in enumerate(cover):
    ax3.axhspan(z_start, z_end, alpha=0.3, color=colors[i], label=f'I_{i}')
ax3.set_title('Filter f(X)=z with Overlapping Cover\n(∅ Subsets Possible if Empty Interval)')
ax3.set_xlabel('Point Index'); ax3.set_ylabel('z')
ax3.legend(); plt.tight_layout(); plt.show()

print(f"X has {len(X)} points (manifold approx); T starts with {len(pullbacks)} non-empty U_i ⊆ X")
