# manifold_demo.py
# Minimal, runnable illustrations of embedded manifolds and local coordinates.
# Navigation: Use LEFT/RIGHT arrow keys

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class ManifoldNavigator:
    """Navigate through multiple manifold visualizations."""
    
    def __init__(self):
        self.current_index = 0
        self.plot_titles = [
            "1D manifold (circle) embedded in ℝ²",
            "2D manifold (sphere) embedded in ℝ³",
            "Two nearby points via local chart on sphere",
            "Swiss roll: 2D manifold in ℝ³ + Isomap to ℝ²"
        ]
        self.fig = plt.figure(figsize=(10, 7))
        
        # Disable default arrow key bindings (they navigate plot history by default)
        for key in ['left', 'right', 'up', 'down']:
            if key in plt.rcParams['keymap.back']:
                plt.rcParams['keymap.back'].remove(key)
            if key in plt.rcParams['keymap.forward']:
                plt.rcParams['keymap.forward'].remove(key)
        
        # Connect key press event
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        
        self.update_plot()
    
    def on_key(self, event):
        """Handle arrow key navigation."""
        print(f"Key pressed: '{event.key}'")  # Debug output
        
        if event.key in ['right', 'Right']:
            self.current_index = (self.current_index + 1) % 4
            self.update_plot()
        elif event.key in ['left', 'Left']:
            self.current_index = (self.current_index - 1) % 4
            self.update_plot()
    
    def update_plot(self):
        """Update the current visualization."""
        self.fig.clear()
        
        if self.current_index == 0:
            self.plot_circle()
        elif self.current_index == 1:
            self.plot_sphere()
        elif self.current_index == 2:
            self.plot_sphere_points()
        elif self.current_index == 3:
            self.plot_swiss_roll()
        
        nav_text = f"Plot {self.current_index + 1}/4 - Use ← → arrow keys to navigate"
        self.fig.suptitle(nav_text, fontsize=11, fontweight='bold')
        self.fig.canvas.draw()
    
    def plot_circle(self):
        """1D manifold: Circle in R^2."""
        ax = self.fig.add_subplot(111)
        theta = np.linspace(0.0, 2.0 * np.pi, 400)
        x = np.cos(theta)
        y = np.sin(theta)
        
        ax.plot(x, y, linewidth=2)
        ax.set_aspect("equal", adjustable="box")
        ax.set_title(self.plot_titles[0])
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True, alpha=0.3)
    
    def plot_sphere(self):
        """2D manifold: Sphere in R^3."""
        ax = self.fig.add_subplot(111, projection='3d')
        u = np.linspace(0.0, np.pi, 80)
        v = np.linspace(0.0, 2.0 * np.pi, 160)
        U, V = np.meshgrid(u, v)
        
        X = np.sin(U) * np.cos(V)
        Y = np.sin(U) * np.sin(V)
        Z = np.cos(U)
        
        ax.plot_surface(X, Y, Z, alpha=0.8, cmap='viridis')
        ax.set_title(self.plot_titles[1])
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
    
    def plot_sphere_points(self):
        """Local chart: Two points on sphere."""
        ax = self.fig.add_subplot(111, projection='3d')
        
        # Coarse sphere for context
        u = np.linspace(0.0, np.pi, 30)
        v = np.linspace(0.0, 2.0 * np.pi, 60)
        U, V = np.meshgrid(u, v)
        X = np.sin(U) * np.cos(V)
        Y = np.sin(U) * np.sin(V)
        Z = np.cos(U)
        ax.plot_surface(X, Y, Z, alpha=0.3, color='lightblue')
        
        # Two nearby points
        u0, v0 = np.pi / 4.0, np.pi / 4.0
        du, dv = 0.05, 0.00
        
        p = self.sphere_chart(u0, v0)
        q = self.sphere_chart(u0 + du, v0 + dv)
        
        ax.scatter([p[0]], [p[1]], [p[2]], s=100, c='red', marker='o', label='Point p')
        ax.scatter([q[0]], [q[1]], [q[2]], s=100, c='green', marker='o', label='Point q')
        ax.plot([p[0], q[0]], [p[1], q[1]], [p[2], q[2]], 'r-', linewidth=2)
        
        ambient_distance = np.linalg.norm(p - q)
        ax.set_title(f"{self.plot_titles[2]}\nAmbient distance: {ambient_distance:.4f}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        ax.legend()
    
    def sphere_chart(self, u, v):
        """Local coordinates (u,v) -> ambient point on unit sphere."""
        return np.array([
            np.sin(u) * np.cos(v),
            np.sin(u) * np.sin(v),
            np.cos(u),
        ])
    
    def plot_swiss_roll(self):
        """Swiss roll with Isomap embedding."""
        try:
            from sklearn.datasets import make_swiss_roll
            from sklearn.manifold import Isomap
        except ImportError:
            ax = self.fig.add_subplot(111)
            ax.text(0.5, 0.5, 'scikit-learn not available\nInstall with: pip install scikit-learn',
                   ha='center', va='center', fontsize=14, transform=ax.transAxes)
            ax.set_title(self.plot_titles[3])
            return
        
        # Generate Swiss roll
        X, _ = make_swiss_roll(n_samples=2000, noise=0.05, random_state=0)
        
        # Create side-by-side subplots
        ax1 = self.fig.add_subplot(121, projection='3d')
        ax1.scatter(X[:, 0], X[:, 1], X[:, 2], s=5, c=X[:, 0], cmap='viridis')
        ax1.set_title("Swiss roll (3D)")
        ax1.set_xlabel("x")
        ax1.set_ylabel("y")
        ax1.set_zlabel("z")
        
        # Isomap embedding
        iso = Isomap(n_neighbors=10, n_components=2)
        X_iso = iso.fit_transform(X)
        
        ax2 = self.fig.add_subplot(122)
        ax2.scatter(X_iso[:, 0], X_iso[:, 1], s=5, c=X[:, 0], cmap='viridis')
        ax2.set_aspect("equal", adjustable="box")
        ax2.set_title("Isomap embedding (2D chart)")
        ax2.set_xlabel("coord 1")
        ax2.set_ylabel("coord 2")


def main():
    print("\n" + "="*60)
    print("MANIFOLD DEMO - Interactive Navigation")
    print("="*60)
    print("\nUse LEFT/RIGHT arrow keys to navigate between examples:")
    print("  1. Circle (1D manifold in ℝ²)")
    print("  2. Sphere (2D manifold in ℝ³)")
    print("  3. Local chart distance on sphere")
    print("  4. Swiss roll + Isomap (2D in ℝ³ → ℝ²)")
    print("\nThe terminal will show 'Key pressed' when you press keys.")
    print("Close the window to exit.")
    print("="*60 + "\n")
    
    navigator = ManifoldNavigator()
    plt.show()


if __name__ == "__main__":
    main()
