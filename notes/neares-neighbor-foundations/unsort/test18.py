import matplotlib.pyplot as plt

# Define X and T properly as sets
X = {'p'}  # Single point (0D manifold approx) - use set
T = [set(), X]  # Opens: ∅ and {p}

fig, ax = plt.subplots()
ax.scatter(0, 0, c='blue', s=100, label='Point p in X')  # Plot as dot
ax.add_patch(plt.Circle((0, 0), 0.1, fill=False, color='red', label='Open {p} ∈ T'))  # Neighborhood visualization
ax.text(0.2, 0, '∅ open (vacuous)', fontsize=10)
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_title('1-Point Topology: (X={p}, T={∅, {p}})')
ax.legend()
ax.axis('off')
plt.show()

print("Axioms: Unions/Intersections stay in T; approximates manifold locally.")
