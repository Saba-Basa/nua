# torus_example_improved.py
# Demonstration of a torus as a 2D manifold with overlapping coordinate charts

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  # needed for 3d projection


# Torus parameters
R = 3  # Major radius
r = 1  # Minor radius

# Create figure
fig = plt.figure(figsize=(12, 8))
fig.suptitle('Torus T² as a 2D Smooth Manifold', fontsize=14, fontweight='bold')

# ========================================
# LEFT: Torus with overlapping chart regions
# ========================================
ax = fig.add_subplot(121, projection='3d')

# Full torus (transparent base)
u_full = np.linspace(0, 2*np.pi, 100)
v_full = np.linspace(0, 2*np.pi, 100)
U_full, V_full = np.meshgrid(u_full, v_full)

X_full = (R + r*np.cos(V_full)) * np.cos(U_full)
Y_full = (R + r*np.cos(V_full)) * np.sin(U_full)
Z_full = r * np.sin(V_full)

ax.plot_surface(X_full, Y_full, Z_full, alpha=0.15, color='lightgray', edgecolor='none')

# --- Chart region 1: U_i (cyan) ---
# Parameter domain: (u, v) in [0, 1.3π] × [0, 1.3π]
u1 = np.linspace(0, 1.3*np.pi, 40)
v1 = np.linspace(0, 1.3*np.pi, 40)
U1, V1 = np.meshgrid(u1, v1)

X1 = (R + r*np.cos(V1)) * np.cos(U1)
Y1 = (R + r*np.cos(V1)) * np.sin(U1)
Z1 = r * np.sin(V1)

ax.plot_surface(X1, Y1, Z1, alpha=0.6, color='cyan', edgecolor='none')

# --- Chart region 2: U_j (yellow) ---
# Parameter domain: (u, v) in [0.7π, 2π] × [0.7π, 2π]
u2 = np.linspace(0.7*np.pi, 2*np.pi, 40)
v2 = np.linspace(0.7*np.pi, 2*np.pi, 40)
U2, V2 = np.meshgrid(u2, v2)

X2 = (R + r*np.cos(V2)) * np.cos(U2)
Y2 = (R + r*np.cos(V2)) * np.sin(U2)
Z2 = r * np.sin(V2)

ax.plot_surface(X2, Y2, Z2, alpha=0.6, color='yellow', edgecolor='none')

# --- Overlap region: U_i ∩ U_j (green) ---
# Parameter domain intersection in (u, v):
# u in [0.7π, 1.3π], v in [0.7π, 1.3π]
u_overlap = np.linspace(0.7*np.pi, 1.3*np.pi, 30)
v_overlap = np.linspace(0.7*np.pi, 1.3*np.pi, 30)
U_overlap, V_overlap = np.meshgrid(u_overlap, v_overlap)

X_overlap = (R + r*np.cos(V_overlap)) * np.cos(U_overlap)
Y_overlap = (R + r*np.cos(V_overlap)) * np.sin(U_overlap)
Z_overlap = r * np.sin(V_overlap)

ax.plot_surface(X_overlap, Y_overlap, Z_overlap, alpha=0.9, color='green', edgecolor='none')

ax.set_title('Two Overlapping Charts on the Torus\n'
             '(Cyan: $U_i$, Yellow: $U_j$, Green: $U_i \\cap U_j$)',
             fontsize=11, pad=20)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(elev=20, azim=45)

# ========================================
# RIGHT: Explanation
# ========================================
ax2 = fig.add_subplot(122)
ax2.axis('off')

explanation = r"""
TORUS T² AS A 2D MANIFOLD

The (standard) torus T² is a 2-dimensional smooth
manifold which can be embedded in ℝ³.

PARAMETRIZATION (GLOBAL COORDINATES):
  u ∈ [0, 2π]  – major angle (around the ring)
  v ∈ [0, 2π]  – minor angle (around the tube)

  x(u, v) = (R + r·cos v)·cos u
  y(u, v) = (R + r·cos v)·sin u
  z(u, v) =  r·sin v

Each point on the torus is given by some (u, v).

CHARTS (LOCAL COORDINATES):

• Chart φᵢ : (0, 1.3π) × (0, 1.3π) ⊂ ℝ² → Uᵢ ⊂ T²   (cyan)
  This is the image of the first parameter patch.

• Chart φⱼ : (0.7π, 2π) × (0.7π, 2π) ⊂ ℝ² → Uⱼ ⊂ T²  (yellow)

OVERLAP (green):
• Uᵢ ∩ Uⱼ = region of the torus covered by both charts.
• In parameters: u ∈ (0.7π, 1.3π), v ∈ (0.7π, 1.3π).

TRANSITION MAP (CHANGE OF COORDINATES):

  φⱼ ∘ φᵢ⁻¹ :
      φᵢ(Uᵢ ∩ Uⱼ) ⊂ ℝ²  →  φⱼ(Uᵢ ∩ Uⱼ) ⊂ ℝ²

This map takes local coordinates from chart φᵢ
and expresses the same points in coordinates of φⱼ.
For a smooth manifold, all such transition maps
must be smooth (C^∞).

INTRINSIC vs AMBIENT DIMENSION:
• Intrinsic dimension: 2 (local coordinates (u, v))
• Ambient dimension:    3 (embedded in ℝ³)
"""

ax2.text(0.05, 0.95, explanation, transform=ax2.transAxes,
         fontsize=9.5, verticalalignment='top', family='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.show()
