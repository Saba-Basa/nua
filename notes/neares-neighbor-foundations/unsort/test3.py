import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap

# === 1) Torus manifold (2D) eingebettet in 4D ==================
n = 800
theta = np.random.rand(n) * 2 * np.pi  # Winkel um das Loch
phi   = np.random.rand(n) * 2 * np.pi  # Winkel um die Röhre
R, r  = 2.0, 0.6                       # großer & kleiner Radius

# Eingebettet in 4D -> (x1,x2,x3,x4)
X = np.column_stack([
    (R + r*np.cos(phi)) * np.cos(theta),   # x1
    (R + r*np.cos(phi)) * np.sin(theta),   # x2
    r*np.sin(phi),                         # x3
    0.3 * np.sin(2*theta)                  # x4 = zusätzliche Messgröße
])

# === 2) "Entfaltung" mit Isomap ==================================
X_iso = Isomap(n_neighbors=12, n_components=2).fit_transform(X)

# === 3) Plot =====================================================
fig = plt.figure(figsize=(10,4))

# 3D-Ausschnitt (erste drei Koordinaten)
ax = fig.add_subplot(121, projection="3d")
ax.scatter(X[:,0], X[:,1], X[:,2], c=theta, cmap='twilight', s=10)
ax.set_title("Torus-Manifold in ℝ⁴ (3D-Ansicht)")
ax.set_xlabel("x₁"); ax.set_ylabel("x₂"); ax.set_zlabel("x₃")

# 2D-Einbettung
ax2 = fig.add_subplot(122)
ax2.scatter(X_iso[:,0], X_iso[:,1], c=theta, cmap='twilight', s=10)
ax2.set_title("Isomap-Einbettung (≈ intrinsische 2D-Struktur)")
ax2.set_xlabel("Komponente 1"); ax2.set_ylabel("Komponente 2")

plt.tight_layout()
plt.show()
