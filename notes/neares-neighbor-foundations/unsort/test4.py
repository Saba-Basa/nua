import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap

# === 1) Torus manifold (2D) eingebettet in 4D ==================
n = 800
theta = np.random.rand(n) * 2 * np.pi  # Winkel um das Loch
phi   = np.random.rand(n) * 2 * np.pi  # Winkel um die Röhre
R, r  = 2.0, 0.6                       # großer & kleiner Radius

# Eingebettet in 4D (Beobachtungsraum)
X = np.column_stack([
    (R + r*np.cos(phi)) * np.cos(theta),   # x1
    (R + r*np.cos(phi)) * np.sin(theta),   # x2
    r*np.sin(phi),                         # x3
    0.3 * np.sin(2*theta)                  # x4 = Zusatzfeature
])

# === 2) Isomap-Einbettung =======================================
X_iso = Isomap(n_neighbors=12, n_components=2).fit_transform(X)

# === 3) Zwei Punkte (Patienten) auswählen =======================
iA, iB = 120, 180
xA, xB = X[iA], X[iB]
zA, zB = X_iso[iA], X_iso[iB]

# === 4) Plot =====================================================
fig = plt.figure(figsize=(10,4))

# --- (a) 3D-Ansicht (Rohdaten) ---
ax = fig.add_subplot(121, projection="3d")
ax.scatter(X[:,0], X[:,1], X[:,2], c=theta, cmap='twilight', s=10, alpha=0.6)
ax.scatter(xA[0], xA[1], xA[2], color='red', s=60, label='Patient A')
ax.scatter(xB[0], xB[1], xB[2], color='gold', s=60, label='Patient B')
ax.plot([xA[0], xB[0]], [xA[1], xB[1]], [xA[2], xB[2]], 'gray', linestyle='--', alpha=0.6)
ax.set_title("Rohmerkmale in ℝ⁴ (3D-Ausschnitt)")
ax.set_xlabel("x₁"); ax.set_ylabel("x₂"); ax.set_zlabel("x₃")
ax.legend()

# --- (b) 2D Isomap-Einbettung ---
ax2 = fig.add_subplot(122)
ax2.scatter(X_iso[:,0], X_iso[:,1], c=theta, cmap='twilight', s=10, alpha=0.6)
ax2.scatter(zA[0], zA[1], color='red', s=60)
ax2.scatter(zB[0], zB[1], color='gold', s=60)
ax2.plot([zA[0], zB[0]], [zA[1], zB[1]], 'gray', linestyle='--', alpha=0.6)
ax2.set_title("Isomap-Einbettung (≈ intrinsische 2D-Struktur)")
ax2.set_xlabel("Komponente 1"); ax2.set_ylabel("Komponente 2")

plt.tight_layout()
plt.show()
