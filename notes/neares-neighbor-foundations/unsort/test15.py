# torus_example_improved.py
# Demonstration of a torus as a 2D manifold with overlapping coordinate charts

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  # needed for 3d projection
from matplotlib.patches import Rectangle


# Torus parameters
R = 3  # Major radius
r = 1  # Minor radius

# Chart domains in parameter space
u1_min, u1_max = 0.0, 1.3 * np.pi
v1_min, v1_max = 0.0, 1.3 * np.pi

u2_min, u2_max = 0.7 * np.pi, 2.0 * np.pi
v2_min, v2_max = 0.7 * np.pi, 2.0 * np.pi

u_overlap_min, u_overlap_max = 0.7 * np.pi, 1.3 * np.pi
v_overlap_min, v_overlap_max = 0.7 * np.pi, 1.3 * np.pi

# Create figure
fig = plt.figure(figsize=(16, 8))
fig.suptitle('Torus T² as a 2D Smooth Manifold', fontsize=14, fontweight='bold')

# ========================================
# LEFT: Torus with overlapping chart regions
# ========================================
ax1 = fig.add_subplot(131, projection='3d')

# Full torus (transparent base)
u_full = np.linspace(0, 2*np.pi, 100)
v_full = np.linspace(0, 2*np.pi, 100)
U_full, V_full = np.meshgrid(u_full, v_full)

X_full = (R + r*np.cos(V_full)) * np.cos(U_full)
Y_full = (R + r*np.cos(V_full)) * np.sin(U_full)
Z_full = r * np.sin(V_full)

ax1.plot_surface(X_full, Y_full, Z_full, alpha=0.15, color='lightgray', edgecolor='none')

# --- Chart region 1: U_i (cyan) ---
u1 = np.linspace(u1_min, u1_max, 40)
v1 = np.linspace(v1_min, v1_max, 40)
U1, V1 = np.meshgrid(u1, v1)

X1 = (R + r*np.cos(V1)) * np.cos(U1)
Y1 = (R + r*np.cos(V1)) * np.sin(U1)
Z1 = r * np.sin(V1)

ax1.plot_surface(X1, Y1, Z1, alpha=0.6, color='cyan', edgecolor='none')

# --- Chart region 2: U_j (yellow) ---
u2 = np.linspace(u2_min, u2_max, 40)
v2 = np.linspace(v2_min, v2_max, 40)
U2, V2 = np.meshgrid(u2, v2)

X2 = (R + r*np.cos(V2)) * np.cos(U2)
Y2 = (R + r*np.cos(V2)) * np.sin(U2)
Z2 = r * np.sin(V2)

ax1.plot_surface(X2, Y2, Z2, alpha=0.6, color='yellow', edgecolor='none')

# --- Overlap region: U_i ∩ U_j (green) ---
u_overlap = np.linspace(u_overlap_min, u_overlap_max, 30)
v_overlap = np.linspace(v_overlap_min, v_overlap_max, 30)
U_overlap, V_overlap = np.meshgrid(u_overlap, v_overlap)

X_overlap = (R + r*np.cos(V_overlap)) * np.cos(U_overlap)
Y_overlap = (R + r*np.cos(V_overlap)) * np.sin(U_overlap)
Z_overlap = r * np.sin(V_overlap)

ax1.plot_surface(X_overlap, Y_overlap, Z_overlap, alpha=0.9, color='green', edgecolor='none')

ax1.set_title('Charts on the Torus Surface\n'
              '(Cyan: $U_i$, Yellow: $U_j$, Green: $U_i \\cap U_j$)',
              fontsize=11, pad=20)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.view_init(elev=20, azim=45)

# ========================================
# MIDDLE: Unfolded chart domains in (u, v)-space
# ========================================
ax2 = fig.add_subplot(132)
ax2.set_aspect('equal', adjustable='box')

# Chart φ_i (cyan)
rect_i = Rectangle((u1_min, v1_min),
                   u1_max - u1_min,
                   v1_max - v1_min,
                   facecolor='cyan', alpha=0.3,
                   edgecolor='black', linewidth=1.0, label='$U_i$')

# Chart φ_j (yellow)
rect_j = Rectangle((u2_min, v2_min),
                   u2_max - u2_min,
                   v2_max - v2_min,
                   facecolor='yellow', alpha=0.3,
                   edgecolor='black', linewidth=1.0, label='$U_j$')

# Overlap (green)
rect_overlap = Rectangle((u_overlap_min, v_overlap_min),
                         u_overlap_max - u_overlap_min,
                         v_overlap_max - v_overlap_min,
                         facecolor='green', alpha=0.6,
                         edgecolor='black', linewidth=1.0, label='$U_i \\cap U_j$')

ax2.add_patch(rect_i)
ax2.add_patch(rect_j)
ax2.add_patch(rect_overlap)

ax2.set_xlim(0, 2*np.pi)
ax2.set_ylim(0, 2*np.pi)
ax2.set_xlabel(r'$u$ (angle around the ring)')
ax2.set_ylabel(r'$v$ (angle around the tube)')
ax2.set_title('Chart Domains in Parameter Space $(u,v)$')

ax2.set_xticks([0, np.pi, 2*np.pi])
ax2.set_xticklabels(['0', r'$\pi$', r'$2\pi$'])
ax2.set_yticks([0, np.pi, 2*np.pi])
ax2.set_yticklabels(['0', r'$\pi$', r'$2\pi$'])

ax2.legend(loc='upper right', frameon=True)

# ========================================
# RIGHT: Text explanation
# ========================================
ax3 = fig.add_subplot(133)
ax3.axis('off')

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

ax3.text(0.02, 0.98, explanation, transform=ax3.transAxes,
         fontsize=9.0, verticalalignment='top', family='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.show()
