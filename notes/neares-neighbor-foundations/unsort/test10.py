#!/usr/bin/env python3
"""
Visualize Differential Manifold with Coordinate Charts
Creates a 3D torus visualization with overlapping patches like the diagram
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d.proj3d import proj_transform

class Arrow3D(FancyArrowPatch):
    def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._xyz = (x, y, z)
        self._dxdydz = (dx, dy, dz)
        self._verts3d = ([x, x + dx], [y, y + dy], [z, z + dz])

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

def create_torus(R=3, r=1, num_points=50):
    """Create torus surface"""
    u = np.linspace(0, 2 * np.pi, num_points)
    v = np.linspace(0, 2 * np.pi, num_points)
    u, v = np.meshgrid(u, v)
    
    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)
    
    return x, y, z, u, v

def create_patch(u_center, v_center, u_range=0.8, v_range=0.8, R=3, r=1, num_points=15):
    """Create a local patch on the torus"""
    u = np.linspace(u_center - u_range, u_center + u_range, num_points)
    v = np.linspace(v_center - v_range, v_center + v_range, num_points)
    u, v = np.meshgrid(u, v)
    
    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)
    
    return x, y, z

def create_coordinate_plane(center_x, center_y, size=1.5):
    """Create a flat coordinate plane for chart visualization"""
    x = np.linspace(center_x - size, center_x + size, 10)
    y = np.linspace(center_y - size, center_y + size, 10)
    X, Y = np.meshgrid(x, y)
    Z = np.ones_like(X) * -5 
    return X, Y, Z

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

R, r = 3, 1
x_torus, y_torus, z_torus, u_torus, v_torus = create_torus(R, r)

ax.plot_surface(x_torus, y_torus, z_torus, 
                color='lightgray', alpha=0.2, 
                edgecolor='gray', linewidth=0.1)

u_i_center, v_i_center = np.pi/3, np.pi/4
x_i, y_i, z_i = create_patch(u_i_center, v_i_center, R=R, r=r)
ax.plot_surface(x_i, y_i, z_i, color='blue', alpha=0.5, edgecolor='darkblue', linewidth=0.5)

u_j_center, v_j_center = np.pi/2, np.pi/4
x_j, y_j, z_j = create_patch(u_j_center, v_j_center, R=R, r=r)
ax.plot_surface(x_j, y_j, z_j, color='yellow', alpha=0.5, edgecolor='orange', linewidth=0.5)

q_i_u, q_i_v = u_i_center, v_i_center
q_i = np.array([
    (R + r * np.cos(q_i_v)) * np.cos(q_i_u),
    (R + r * np.cos(q_i_v)) * np.sin(q_i_u),
    r * np.sin(q_i_v)
])

q_j_u, q_j_v = u_j_center, v_j_center
q_j = np.array([
    (R + r * np.cos(q_j_v)) * np.cos(q_j_u),
    (R + r * np.cos(q_j_v)) * np.sin(q_j_u),
    r * np.sin(q_j_v)
])

ax.scatter(*q_i, color='darkblue', s=100, marker='o', edgecolors='black', linewidth=2)
ax.scatter(*q_j, color='darkorange', s=100, marker='o', edgecolors='black', linewidth=2)

ax.text(q_i[0], q_i[1], q_i[2]+0.5, r'$q_i$', fontsize=14, fontweight='bold')
ax.text(q_j[0], q_j[1], q_j[2]+0.5, r'$q_j$', fontsize=14, fontweight='bold')
ax.text(0, 0, 2.5, r'$\mathcal{D}$', fontsize=18, fontweight='bold')

X_chart_i, Y_chart_i, Z_chart_i = create_coordinate_plane(-5, 0)
ax.plot_surface(X_chart_i, Y_chart_i, Z_chart_i, color='lightblue', alpha=0.4, edgecolor='blue')
ax.text(-5, 0, -5.5, r'$\phi_i(U_i)$', fontsize=12, ha='center')

X_chart_j, Y_chart_j, Z_chart_j = create_coordinate_plane(5, 0)
ax.plot_surface(X_chart_j, Y_chart_j, Z_chart_j, color='lightyellow', alpha=0.4, edgecolor='orange')
ax.text(5, 0, -5.5, r'$\phi_j(U_j)$', fontsize=12, ha='center')

ax.scatter(-5, 0, -5, color='darkblue', s=80, marker='o')
ax.scatter(5, 0, -5, color='darkorange', s=80, marker='o')

arrow = Arrow3D(-3.5, 0, -5, 7, 0, 0,
                mutation_scale=20, lw=2, arrowstyle='-|>', color='purple')
ax.add_artist(arrow)
ax.text(1, 0, -4, r'$\phi_{ij} = \phi_j \circ \phi_i^{-1}$', 
        fontsize=11, color='purple', fontweight='bold')

arrow_i = Arrow3D(q_i[0], q_i[1], q_i[2], -5-q_i[0], -q_i[1], -5-q_i[2],
                  mutation_scale=15, lw=1.5, arrowstyle='->', color='red', linestyle='--')
ax.add_artist(arrow_i)
ax.text((q_i[0]-5)/2, q_i[1]/2, (q_i[2]-5)/2, r'$\phi_i$', 
        fontsize=10, color='red')

arrow_j = Arrow3D(q_j[0], q_j[1], q_j[2], 5-q_j[0], -q_j[1], -5-q_j[2],
                  mutation_scale=15, lw=1.5, arrowstyle='->', color='red', linestyle='--')
ax.add_artist(arrow_j)
ax.text((q_j[0]+5)/2, q_j[1]/2, (q_j[2]-5)/2, r'$\phi_j$', 
        fontsize=10, color='red')

ax.set_xlabel('X', fontsize=10)
ax.set_ylabel('Y', fontsize=10)
ax.set_zlabel('Z', fontsize=10)
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.set_zlim(-6, 4)
ax.view_init(elev=20, azim=45)
ax.set_box_aspect([1, 1, 0.8])

plt.title('Differential Manifold with Coordinate Charts', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

print("✓ Visualization created successfully!")
