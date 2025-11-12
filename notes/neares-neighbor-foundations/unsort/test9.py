import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 80)
y = np.linspace(-3, 3, 80)
X, Y = np.meshgrid(x, y)
Z = 0.5 * np.sin(X)

x0, y0 = 0, 0
z0 = 0.5 * np.sin(x0)

ix = (np.abs(x - x0)).argmin()
iy = (np.abs(y - y0)).argmin()
r = 10
X_patch = X[iy-r:iy+r, ix-r:ix+r]
Y_patch = Y[iy-r:iy+r, ix-r:ix+r]
Z_patch = Z[iy-r:iy+r, ix-r:ix+r]

tangent_Z = z0 + 0.5 * (X - x0)

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, tangent_Z, alpha=0.3, color='lightgray', edgecolor='gray', linewidth=0.3)
ax.plot_surface(X, Y, Z, alpha=0.25, color='lightblue', edgecolor='none')
ax.plot_surface(X_patch, Y_patch, Z_patch, color='darkorange', alpha=1.0, edgecolor='black', linewidth=0.5)
ax.scatter(x0, y0, z0, color='red', s=250, zorder=10, edgecolors='black', linewidths=2)
ax.text(x0-0.3, y0-0.8, z0 + 0.3, "x ∈ M", color='red', fontsize=16, weight='bold')
ax.text(2, 2, 0, "TₓM", color='gray', fontsize=14, weight='bold')

ax.set_title("Manifold M ⊂ ℝ³ with Local Neighborhood U and Tangent Plane TₓM", 
             fontsize=16, pad=20, weight='bold')
ax.set_xlabel("x", fontsize=13)
ax.set_ylabel("y", fontsize=13)
ax.set_zlabel("z", fontsize=13)

ax.view_init(elev=15, azim=45)
ax.set_zlim(-1.5, 1.5)

plt.tight_layout()
plt.show()
