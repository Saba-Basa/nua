# manifold_demo.py
# Minimal, runnable illustrations of embedded manifolds and local coordinates.
# Shows BOTH the embedded view AND the parameter space to clarify dimensions.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button


class ManifoldNavigator:
    """Navigate through multiple manifold visualizations using buttons."""
    
    def __init__(self):
        self.current_index = 0
        self.plot_titles = [
            "Circle: 1D manifold embedded in ℝ²",
            "Sphere: 2D manifold embedded in ℝ³",
            "Coordinate Grid on Sphere",
            "Swiss roll: 2D manifold in ℝ³ + Isomap"
        ]
        
        self.fig = plt.figure(figsize=(15, 7))
        self.setup_buttons()
        self.update_plot()
    
    def setup_buttons(self):
        """Create the navigation buttons."""
        ax_prev = plt.axes([0.35, 0.02, 0.12, 0.04])
        self.btn_prev = Button(ax_prev, '← Previous', color='lightblue', hovercolor='skyblue')
        self.btn_prev.on_clicked(self.prev_plot)
        
        ax_next = plt.axes([0.53, 0.02, 0.12, 0.04])
        self.btn_next = Button(ax_next, 'Next →', color='lightblue', hovercolor='skyblue')
        self.btn_next.on_clicked(self.next_plot)
    
    def next_plot(self, event):
        """Show next plot."""
        self.current_index = (self.current_index + 1) % 4
        print(f"Showing plot {self.current_index + 1}/4")
        self.update_plot()
    
    def prev_plot(self, event):
        """Show previous plot."""
        self.current_index = (self.current_index - 1) % 4
        print(f"Showing plot {self.current_index + 1}/4")
        self.update_plot()
    
    def update_plot(self):
        """Update the current visualization."""
        self.fig.clear()
        
      
        self.setup_buttons()
        

        self.fig.subplots_adjust(bottom=0.1, top=0.92, left=0.05, right=0.95, wspace=0.35)
        

        if self.current_index == 0:
            self.plot_circle()
        elif self.current_index == 1:
            self.plot_sphere()
        elif self.current_index == 2:
            self.plot_sphere_points()
        elif self.current_index == 3:
            self.plot_swiss_roll()
        
        nav_text = f"Plot {self.current_index + 1}/4: {self.plot_titles[self.current_index]}"
        self.fig.suptitle(nav_text, fontsize=14, fontweight='bold', y=0.97)
        self.fig.canvas.draw()
    
    def plot_circle(self):
        """1D manifold: Circle - show both embedded and parameter space."""

        ax1 = self.fig.add_subplot(121)
        theta = np.linspace(0.0, 2.0 * np.pi, 400)

        ax1.plot(theta, np.zeros_like(theta), 'b-', linewidth=3)
        ax1.scatter([0, 2*np.pi], [0, 0], c='red', s=100, zorder=5)
        ax1.set_xlim(-0.5, 2*np.pi + 0.5)
        ax1.set_ylim(-0.5, 0.5)
        ax1.set_xlabel('θ (angle parameter)', fontsize=11)
        ax1.set_yticks([])
        ax1.set_title('1D Parameter Space\n(intrinsic dimension = 1)', fontsize=11, pad=10)
        ax1.grid(True, alpha=0.3)
        ax1.axhline(0, color='k', linewidth=0.5)
        ax1.text(np.pi, -0.3, 'Only 1 parameter needed!', 
                ha='center', fontsize=9, style='italic', color='darkblue')
        
        # Right: Embedded circle in 2D
        ax2 = self.fig.add_subplot(122)
        x = np.cos(theta)
        y = np.sin(theta)
        
        scatter = ax2.scatter(x, y, c=theta, cmap='viridis', s=10)
        ax2.set_aspect("equal", adjustable="box")
        ax2.set_title('Embedded in ℝ²\n(ambient dimension = 2)', fontsize=11, pad=10)
        ax2.set_xlabel("x")
        ax2.set_ylabel("y")
        ax2.grid(True, alpha=0.3)
        
        cbar = plt.colorbar(scatter, ax=ax2)
        cbar.set_label('θ', rotation=0, labelpad=10)
    
    def plot_sphere(self):
        """2D manifold: Sphere - show both embedded and parameter space."""
    
        ax1 = self.fig.add_subplot(121)
        u = np.linspace(0.0, np.pi, 80)
        v = np.linspace(0.0, 2.0 * np.pi, 160)
        U, V = np.meshgrid(u, v)
        
        mesh = ax1.pcolormesh(V, U, U, cmap='viridis', shading='auto')
        ax1.set_xlabel('v (longitude)', fontsize=11)
        ax1.set_ylabel('u (latitude)', fontsize=11)
        ax1.set_title('2D Parameter Space (u, v)\n(intrinsic dimension = 2)', fontsize=11, pad=10)
        ax1.text(np.pi, np.pi/2, 'Two parameters needed!', 
                ha='center', fontsize=9, style='italic', color='white', 
                bbox=dict(boxstyle='round', facecolor='black', alpha=0.5))
        
        # Right: Embedded sphere in 3D
        ax2 = self.fig.add_subplot(122, projection='3d')
        X = np.sin(U) * np.cos(V)
        Y = np.sin(U) * np.sin(V)
        Z = np.cos(U)
        
        surf = ax2.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(U/np.pi), alpha=0.9)
        ax2.set_title('Embedded in ℝ³\n(ambient dimension = 3)', fontsize=11, pad=20)
        ax2.set_xlabel("x", labelpad=8)
        ax2.set_ylabel("y", labelpad=8)
        ax2.set_zlabel("z", labelpad=8)
    
    def plot_sphere_points(self):
        """Local chart: Show coordinate grid on sphere - TWO VIEWS."""

        ax1 = self.fig.add_subplot(121)
        u = np.linspace(0.0, np.pi, 10)
        v = np.linspace(0.0, 2.0 * np.pi, 20)
        U, V = np.meshgrid(u, v)
        
        ax1.scatter(V.flatten(), U.flatten(), s=20, c='blue', alpha=0.5)
        for u_val in u:
            ax1.axhline(u_val, color='blue', alpha=0.3, linewidth=1)
        for v_val in v:
            ax1.axvline(v_val, color='red', alpha=0.3, linewidth=1)
        
        ax1.set_xlabel('v (longitude)', fontsize=11)
        ax1.set_ylabel('u (latitude)', fontsize=11)
        ax1.set_title('2D Grid in Parameter Space', fontsize=11, pad=10)
        ax1.set_xlim(0, 2*np.pi)
        ax1.set_ylim(0, np.pi)

        ax2 = self.fig.add_subplot(122, projection='3d')
        
        u_lines = np.linspace(0, np.pi, 10)
        v_lines = np.linspace(0, 2*np.pi, 20)
        
        for u_val in u_lines:
            v = np.linspace(0, 2*np.pi, 100)
            x = np.sin(u_val) * np.cos(v)
            y = np.sin(u_val) * np.sin(v)
            z = np.cos(u_val) * np.ones_like(v)
            ax2.plot(x, y, z, 'b-', alpha=0.5, linewidth=1.5)
        
        for v_val in v_lines:
            u = np.linspace(0, np.pi, 100)
            x = np.sin(u) * np.cos(v_val)
            y = np.sin(u) * np.sin(v_val)
            z = np.cos(u)
            ax2.plot(x, y, z, 'r-', alpha=0.5, linewidth=1.5)
        
        u_surf = np.linspace(0.0, np.pi, 30)
        v_surf = np.linspace(0.0, 2.0 * np.pi, 60)
        U_surf, V_surf = np.meshgrid(u_surf, v_surf)
        X = np.sin(U_surf) * np.cos(V_surf)
        Y = np.sin(U_surf) * np.sin(V_surf)
        Z = np.cos(U_surf)
        ax2.plot_surface(X, Y, Z, alpha=0.1, color='lightgray')
        
        ax2.set_title('Grid Mapped to Sphere\n(blue=latitude, red=longitude)', fontsize=11, pad=20)
        ax2.set_xlabel("x", labelpad=8)
        ax2.set_ylabel("y", labelpad=8)
        ax2.set_zlabel("z", labelpad=8)
    
    def plot_swiss_roll(self):
        """Swiss roll with Isomap embedding."""
        try:
            from sklearn.datasets import make_swiss_roll
            from sklearn.manifold import Isomap
        except ImportError:
            ax = self.fig.add_subplot(111)
            ax.text(0.5, 0.5, 'scikit-learn not available\nInstall with: pip install scikit-learn',
                   ha='center', va='center', fontsize=14, transform=ax.transAxes)
            return
        
        X, color = make_swiss_roll(n_samples=2000, noise=0.05, random_state=0)
        
        ax1 = self.fig.add_subplot(121, projection='3d')
        ax1.scatter(X[:, 0], X[:, 1], X[:, 2], s=5, c=color, cmap='viridis')
        ax1.set_title("2D Manifold Embedded in ℝ³\n(ambient dimension = 3)", fontsize=11, pad=20)
        ax1.set_xlabel("x", labelpad=8)
        ax1.set_ylabel("y", labelpad=8)
        ax1.set_zlabel("z", labelpad=8)
        
        iso = Isomap(n_neighbors=10, n_components=2)
        X_iso = iso.fit_transform(X)
        
        ax2 = self.fig.add_subplot(122)
        ax2.scatter(X_iso[:, 0], X_iso[:, 1], s=5, c=color, cmap='viridis')
        ax2.set_aspect("equal", adjustable="box")
        ax2.set_title("Recovered 2D Parameters (Isomap)\n(intrinsic dimension = 2)", fontsize=11, pad=10)
        ax2.set_xlabel("coord 1")
        ax2.set_ylabel("coord 2")


def main():
    print("\n" + "="*60)
    print("MANIFOLD DEMO - Intrinsic vs Ambient Dimensions")
    print("="*60)
    print("\nClick Previous/Next to see:")
    print("  1. Circle: 1D parameter (θ) → 2D embedding")
    print("  2. Sphere: 2D parameters (u,v) → 3D embedding")
    print("  3. Parameter grid → Sphere coordinate grid")
    print("  4. Swiss roll: 2D intrinsic → 3D embedding → 2D recovery")
    print("\nKey concept: Dimension = # of parameters needed locally")
    print("="*60 + "\n")
    
    navigator = ManifoldNavigator()
    plt.show()


if __name__ == "__main__":
    main()
