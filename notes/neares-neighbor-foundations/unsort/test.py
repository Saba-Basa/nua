# -*- coding: utf-8 -*-
# Visualize how manifold embedding (Isomap) can change neighborhood relations.
# Highlights two pairs:
#  A (red): close in raw 2D features but far on the intrinsic 2D manifold.
#  B (green): far in raw 2D features but close on the intrinsic 2D manifold.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap

def main():
    # ---------- 1) Synthetic patients ----------
    # d = 8 measured features; intrinsic m ≈ 2 latent factors
    n = 400
    rng = np.random.default_rng(42)

    latent = rng.standard_normal((n, 2))  # m=2
    # mixing from 2 latent factors to 8 observed features (heterogeneous scales)
    W = rng.standard_normal((2, 8)) * np.array([1.0, 0.8, 0.6, 0.5, 0.7, 0.4, 0.3, 0.2])
    X = latent @ W + 0.05 * rng.standard_normal((n, 8))  # add small measurement noise

    # ---------- 2) Isomap embedding to 2D ----------
    emb = Isomap(n_neighbors=12, n_components=2).fit_transform(X)

    # ---------- 3) Distances ----------
    raw2 = X[:, :2]  # show only first two observed features (e.g., BP & HR)
    D_raw = np.linalg.norm(raw2[:, None, :] - raw2[None, :, :], axis=2)
    D_emb = np.linalg.norm(emb[:, None, :]  - emb[None, :, :],  axis=2)
    np.fill_diagonal(D_raw, np.inf)
    np.fill_diagonal(D_emb, np.inf)

    # ---------- 4) Select illustrative pairs ----------
    # thresholds: "close" = 10th percentile of distances
    q10_raw = np.quantile(D_raw[np.isfinite(D_raw)], 0.10)
    q10_emb = np.quantile(D_emb[np.isfinite(D_emb)], 0.10)

    # Pair A: close in raw (<= q10_raw) but FAR in embedding (maximize D_emb under mask)
    maskA = D_raw <= q10_raw
    iA, jA = np.unravel_index(np.argmax(np.where(maskA, D_emb, -np.inf)), D_emb.shape)

    # Pair B: close in embedding (<= q10_emb) but FAR in raw (maximize D_raw under mask)
    maskB = D_emb <= q10_emb
    iB, jB = np.unravel_index(np.argmax(np.where(maskB, D_raw, -np.inf)), D_raw.shape)

    # ---------- 5) Plot ----------
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    # Left: raw 2D features (only two of the eight)
    ax[0].scatter(raw2[:, 0], raw2[:, 1], s=12, alpha=0.35, color='gray')
    ax[0].plot(raw2[[iA, jA], 0], raw2[[iA, jA], 1], '-o', color='tab:red', lw=2, ms=6, label='Pair A')
    ax[0].plot(raw2[[iB, jB], 0], raw2[[iB, jB], 1], '-o', color='tab:green', lw=2, ms=6, label='Pair B')
    ax[0].set_title("Rohmerkmale (x₁=Blutdruck, x₂=Puls)")
    ax[0].set_xlabel("x₁"); ax[0].set_ylabel("x₂")
    ax[0].legend(loc='upper right', frameon=False)
    ax[0].text(0.02, 0.02,
               f"A: ‖·‖raw={D_raw[iA, jA]:.2f}\nB: ‖·‖raw={D_raw[iB, jB]:.2f}",
               transform=ax[0].transAxes, ha='left', va='bottom')

    # Right: Isomap embedding (≈ intrinsic 2D)
    ax[1].scatter(emb[:, 0], emb[:, 1], s=12, alpha=0.35, color='gray')
    ax[1].plot(emb[[iA, jA], 0], emb[[iA, jA], 1], '-o', color='tab:red', lw=2, ms=6, label='Pair A')
    ax[1].plot(emb[[iB, jB], 0], emb[[iB, jB], 1], '-o', color='tab:green', lw=2, ms=6, label='Pair B')
    ax[1].set_title("Isomap-Einbettung (≈ m=2)")
    ax[1].set_xlabel("Komponente 1"); ax[1].set_ylabel("Komponente 2")
    ax[1].legend(loc='upper right', frameon=False)
    ax[1].text(0.02, 0.02,
               f"A: ‖·‖iso={D_emb[iA, jA]:.2f}\nB: ‖·‖iso={D_emb[iB, jB]:.2f}",
               transform=ax[1].transAxes, ha='left', va='bottom')

    plt.tight_layout()
    plt.show()

    # ---------- 6) Console summary ----------
    print("Pair A (red): close in raw 2D, far in Isomap")
    print(f"  raw distance  = {D_raw[iA, jA]:.3f}")
    print(f"  iso distance  = {D_emb[iA, jA]:.3f}")
    print("Pair B (green): far in raw 2D, close in Isomap")
    print(f"  raw distance  = {D_raw[iB, jB]:.3f}")
    print(f"  iso distance  = {D_emb[iB, jB]:.3f}")

if __name__ == "__main__":
    main()
