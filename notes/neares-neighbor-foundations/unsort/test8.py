import numpy as np

t = np.linspace(0, 4*np.pi, 800)
helix = np.c_[np.cos(t), np.sin(t), t/(2*np.pi)]

print("Ambient space: R^3  -> d = 3")
print("Constructed set M = gamma([0,4π])")
print("Data shape:", helix.shape, "(n points × d coordinates)")
print("First row:", helix[0])
print("Intrinsic dimension here: m = 1  (one parameter t)")
