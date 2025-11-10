from sklearn.datasets import make_swiss_roll
from sklearn.manifold import Isomap
import matplotlib.pyplot as plt

# Swiss Roll: 2D manifold in 3D
X, color = make_swiss_roll(n_samples=1000, noise=0.05)

# Isomap: unfold the manifold
X_iso = Isomap(n_neighbors=12, n_components=2).fit_transform(X)

# Plot: original 3D vs unfolded 2D
fig = plt.figure(figsize=(9,4))
ax = fig.add_subplot(121, projection='3d')
ax.scatter(X[:,0], X[:,1], X[:,2], c=color, cmap='Spectral', s=8)
ax.set_title("Gefaltete 2D-Fläche in 3D (Manifold in ℝ³)")

ax2 = fig.add_subplot(122)
ax2.scatter(X_iso[:,0], X_iso[:,1], c=color, cmap='Spectral', s=8)
ax2.set_title("Entfaltete Fläche (Isomap, 2D)")

plt.tight_layout()
plt.show()
