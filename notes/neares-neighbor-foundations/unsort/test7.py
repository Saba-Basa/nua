# Short demo: m vs d with simple data and an Isomap embedding
# Examples:
# 1) Curve in R^3: m = 1, d = 3  (helix)
# 2) Surface in R^4: m = 2, d = 4 (torus)  → show 2D Isomap
# 3) Whole space: M = R^d ⇒ m = d  (random cloud in R^3)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import Isomap

def est_dim_pca(X, var_threshold=0.95):
    """Return the smallest k s.t. PCA explains >= var_threshold of variance."""
    pca = PCA().fit(X)
    csum = np.cumsum(pca.explained_variance_ratio_)
    k = int(np.searchsorted(csum, var_threshold) + 1)
    return k

# 1) Curve in R^3 (helix): m=1, d=3
t = np.linspace(0, 4*np.pi, 800)
helix = np.c_[np.cos(t), np.sin(t), t/(2*np.pi)]

# 2) Surface in R^4 (torus): m=2, d=4 → visualize with Isomap to 2D
def torus_4d(n=900, R=2.0, r=0.6, seed=0):
    rng = np.random.default_rng(seed)
    theta = rng.random(n) * 2*np.pi
    phi   = rng.random(n) * 2*np.pi
    X4 = np.column_stack([
        (R + r*np.cos(phi)) * np.cos(theta),
        (R + r*np.cos(phi)) * np.sin(theta),
        r*np.sin(phi),
        0.35 * np.sin(2*theta)   # extra feature
    ])
    return X4

X4 = torus_4d(n=1000, seed=42)
iso = Isomap(n_neighbors=12, n_components=2)
Z2 = iso.fit_transform(X4)

# 3) Whole space cloud in R^3: M = R^3 ⇒ m = d = 3
cloud = np.random.default_rng(1).normal(size=(1000, 3))

# Console summary
print("Curve in R^3: m = 1, d = 3  (helix)")
print(f"  PCA estimate m_hat (95% var) = {est_dim_pca(helix):d}")
print("Surface in R^4: m = 2, d = 4  (torus)")
print(f"  PCA estimate m_hat (95% var) on X4 = {est_dim_pca(X4):d}")
print("  Isomap gives a 2D chart of the surface (visual check)")
print("Whole space: M = R^3 ⇒ m = d")
print(f"  PCA estimate m_hat (95% var) on cloud = {est_dim_pca(cloud):d}")

# Plots (compact)
fig = plt.figure(figsize=(11, 4))

ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax1.scatter(helix[:,0], helix[:,1], helix[:,2], s=5, alpha=0.6)
ax1.set_title("Curve in $\\mathbb{R}^3$  (m=1, d=3)")
ax1.set_xlabel("x"); ax1.set_ylabel("y"); ax1.set_zlabel("z")

ax2 = fig.add_subplot(1, 3, 2)
ax2.scatter(Z2[:,0], Z2[:,1], s=6, alpha=0.6)
ax2.set_title("Torus in $\\mathbb{R}^4$ via Isomap (m≈2)")
ax2.set_xlabel("comp 1"); ax2.set_ylabel("comp 2")

ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.scatter(cloud[:,0], cloud[:,1], cloud[:,2], s=5, alpha=0.6)
ax3.set_title("Whole space $\\mathbb{R}^3$  (m=d=3)")
ax3.set_xlabel("x"); ax3.set_ylabel("y"); ax3.set_zlabel("z")

plt.tight_layout()
plt.show()
