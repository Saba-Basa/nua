# -*- coding: utf-8 -*-
# Zeigt PAAR A & PAAR B so, dass man "weiter" vs. "nah" WIRKLICH sieht.
# A (rot): scheinbar nah in Rohdaten (3D-Ausschnitt), aber weit nach Entfaltung (Isomap-2D)
# B (grün): scheinbar weit in Rohdaten, aber nah nach Entfaltung

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap

def torus_4d(n=900, R=2.0, r=0.6, seed=0):
    rng = np.random.default_rng(seed)
    theta = rng.random(n) * 2*np.pi      # um das Loch
    phi   = rng.random(n) * 2*np.pi      # um die Röhre
    X4 = np.column_stack([
        (R + r*np.cos(phi)) * np.cos(theta),   # x1
        (R + r*np.cos(phi)) * np.sin(theta),   # x2
        r*np.sin(phi),                         # x3
        0.35 * np.sin(2*theta)                 # x4 (Extra-Feature)
    ])
    color = theta                             # für konsistente Färbung
    return X4, color

def pair_selection(X3, Z2, q=0.10):
    """Wähle zwei illustrative Paare:
       A: nah in X3 (<= q-Quantil), aber maximal weit in Z2
       B: nah in Z2 (<= q-Quantil), aber maximal weit in X3
    """
    # Distanzmatrizen
    D_raw = np.linalg.norm(X3[:,None,:] - X3[None,:,:], axis=2)
    D_emb = np.linalg.norm(Z2[:,None,:] - Z2[None,:,:], axis=2)

    # Diagonale maskieren
    np.fill_diagonal(D_raw, np.inf)
    np.fill_diagonal(D_emb, np.inf)

    # Schwellen
    q_raw = np.quantile(D_raw[np.isfinite(D_raw)], q)
    q_emb = np.quantile(D_emb[np.isfinite(D_emb)], q)

    # A: nah in Rohdaten, max weit in Embedding
    maskA = D_raw <= q_raw
    A_idx = np.unravel_index(np.argmax(np.where(maskA, D_emb, -np.inf)), D_emb.shape)
    iA, jA = int(A_idx[0]), int(A_idx[1])

    # B: nah in Embedding, max weit in Rohdaten
    maskB = D_emb <= q_emb
    B_idx = np.unravel_index(np.argmax(np.where(maskB, D_raw, -np.inf)), D_raw.shape)
    iB, jB = int(B_idx[0]), int(B_idx[1])

    return (iA, jA, D_raw[iA,jA], D_emb[iA,jA]), (iB, jB, D_raw[iB,jB], D_emb[iB,jB])

def annotate_distance_3d(ax, P, Q, text, color):
    """Beschrifte mittig die 3D-Verbindungsstrecke P-Q mit Distanztext."""
    mid = (P + Q) / 2.0
    ax.text(mid[0], mid[1], mid[2], text, color=color, fontsize=9,
            bbox=dict(boxstyle='round,pad=0.25', fc='white', ec=color, alpha=0.8))

def annotate_distance_2d(ax, p, q, text, color):
    """Beschrifte mittig die 2D-Verbindungsstrecke p-q mit Distanztext."""
    mid = (p + q) / 2.0
    ax.annotate(text, xy=mid, xytext=(5, 5), textcoords='offset points',
                ha='left', va='bottom', color=color,
                bbox=dict(boxstyle='round,pad=0.25', fc='white', ec=color, alpha=0.85))

# ===== HELFER: Messung von m und Distanz-Konzentration =====
def local_growth_exponent(points, idx, qmin=0.02, qmax=0.20, n_r=10):
    """
    Schätze lokale intrinsische Dimension m_hat an Punkt idx via log N(r) ≈ m log r + c.
    points : (n,d) Punkte, idx : Index des Referenzpunkts
    """
    x = points[idx]
    d = np.linalg.norm(points - x, axis=1)
    d = d[d > 0.0]
    d.sort()

    if len(d) < 5:
        return np.nan, np.array([]), np.array([])

    r_min = np.quantile(d, qmin)
    r_max = np.quantile(d, qmax)
    if not np.isfinite(r_min) or not np.isfinite(r_max) or r_min <= 0 or r_max <= r_min:
        return np.nan, np.array([]), np.array([])

    radii = np.geomspace(r_min, r_max, n_r)
    counts = np.array([(d <= r).sum() for r in radii])

    mask = counts > 0
    if mask.sum() < 2:
        return np.nan, radii, counts

    log_r = np.log(radii[mask])
    log_N = np.log(counts[mask])
    m_hat, intercept = np.polyfit(log_r, log_N, 1)
    return float(m_hat), radii, counts

def concentration_stats(points, idx):
    """
    Schnappschuss der Distanz-Konzentration um Punkt idx.
    """
    x = points[idx]
    d = np.linalg.norm(points - x, axis=1)
    d = d[d > 0.0]
    d.sort()
    d_near = d[0]
    d_med  = np.median(d)
    d_far  = d[-1]
    return dict(
        d_nearest=float(d_near),
        d_median=float(d_med),
        d_farthest=float(d_far),
        ratio_near_to_far=float(d_near / d_far),
        ratio_med_to_far=float(d_med / d_far),
    )

def console_explain_growth_and_concentration(X_local, Z_local, iA, iB, tagA="A", tagB="B"):
    """
    Kompakte Konsolen-Erklärung verknüpft mit der Illustration.
    """
    idxs = [(tagA, iA), (tagB, iB)]
    print("\nWHY INTRINSIC DIMENSION MATTERS — MEASURED ON YOUR DATA")
    print("We estimate m from the slope of log N(r) versus log r around a point.")
    for label, idx in idxs:
        m_raw, _, _ = local_growth_exponent(X_local, idx, qmin=0.02, qmax=0.20, n_r=12)
        m_iso, _, _ = local_growth_exponent(Z_local, idx, qmin=0.02, qmax=0.20, n_r=12)

        c_raw = concentration_stats(X_local, idx)
        c_iso = concentration_stats(Z_local, idx)

        print(f"\nPair {label}: local growth exponent m (raw 3D slice) ≈ {m_raw:.2f}")
        print(f"Pair {label}: local growth exponent m (Isomap 2D)   ≈ {m_iso:.2f}")
        print("Interpretation: in the embedding, m is close to 2 for a 2D manifold.")

        print("Distance concentration in raw 3D slice:")
        print(f"  nearest={c_raw['d_nearest']:.3f}  median={c_raw['d_median']:.3f}  farthest={c_raw['d_farthest']:.3f}")
        print(f"  nearest/farthest={c_raw['ratio_near_to_far']:.3f}  median/farthest={c_raw['ratio_med_to_far']:.3f}")

        print("Distance concentration in Isomap 2D:")
        print(f"  nearest={c_iso['d_nearest']:.3f}  median={c_iso['d_median']:.3f}  farthest={c_iso['d_farthest']:.3f}")
        print(f"  nearest/farthest={c_iso['ratio_near_to_far']:.3f}  median/farthest={c_iso['ratio_med_to_far']:.3f}")

# ===== HAUPTPROGRAMM =====
def main():
    # 1) Daten: 2D-Manifold (Torus) in 4D
    X4, color = torus_4d(n=1000, seed=42)
    # Für Roh-Plot nehmen wir 3D-Ausschnitt (x1,x2,x3)
    X3 = X4[:, :3]

    # 2) Entfaltung (Isomap) auf 2D
    iso = Isomap(n_neighbors=12, n_components=2)
    Z2 = iso.fit_transform(X4)

    # 3) Paare wählen (A & B)
    (iA, jA, dA_raw, dA_iso), (iB, jB, dB_raw, dB_iso) = pair_selection(X3, Z2, q=0.10)

    # 4) Plot
    fig = plt.figure(figsize=(11.5, 4.8))

    # Links: Rohmerkmale (3D-Ausschnitt)
    axL = fig.add_subplot(1, 2, 1, projection='3d')
    axL.scatter(X3[:,0], X3[:,1], X3[:,2], c=color, cmap='twilight', s=8, alpha=0.55)
    # Paare einzeichnen
    # A (rot): scheinbar NAH in 3D
    axL.plot([X3[iA,0], X3[jA,0]], [X3[iA,1], X3[jA,1]], [X3[iA,2], X3[jA,2]],
             color='crimson', lw=2.5, label='Pair A (scheinbar nah)')
    axL.scatter(X3[[iA,jA],0], X3[[iA,jA],1], X3[[iA,jA],2], color='crimson', s=40)
    annotate_distance_3d(axL, X3[iA], X3[jA], f"‖·‖raw ≈ {dA_raw:.2f}", color='crimson')

    # B (grün): scheinbar WEIT in 3D
    axL.plot([X3[iB,0], X3[jB,0]], [X3[iB,1], X3[jB,1]], [X3[iB,2], X3[jB,2]],
             color='seagreen', lw=2.5, label='Pair B (scheinbar weit)')
    axL.scatter(X3[[iB,jB],0], X3[[iB,jB],1], X3[[iB,jB],2], color='seagreen', s=40)
    annotate_distance_3d(axL, X3[iB], X3[jB], f"‖·‖raw ≈ {dB_raw:.2f}", color='seagreen')

    axL.set_title("Rohmerkmale (3D-Ausschnitt aus ℝ⁴)")
    axL.set_xlabel("x₁"); axL.set_ylabel("x₂"); axL.set_zlabel("x₃")
    axL.legend(loc='upper left', frameon=False)

    # Rechts: Isomap-Entfaltung (2D)
    axR = fig.add_subplot(1, 2, 2)
    axR.scatter(Z2[:,0], Z2[:,1], c=color, cmap='twilight', s=10, alpha=0.55)
    # Paare einzeichnen
    # A (rot): tatsächlich WEIT in 2D
    axR.plot([Z2[iA,0], Z2[jA,0]], [Z2[iA,1], Z2[jA,1]],
             color='crimson', lw=2.5, label='Pair A (tatsächlich weit)')
    axR.scatter(Z2[[iA,jA],0], Z2[[iA,jA],1], color='crimson', s=40)
    annotate_distance_2d(axR, Z2[iA], Z2[jA], f"‖·‖iso ≈ {dA_iso:.2f}", color='crimson')

    # B (grün): tatsächlich NAH in 2D
    axR.plot([Z2[iB,0], Z2[jB,0]], [Z2[iB,1], Z2[jB,1]],
             color='seagreen', lw=2.5, label='Pair B (tatsächlich nah)')
    axR.scatter(Z2[[iB,jB],0], Z2[[iB,jB],1], color='seagreen', s=40)
    annotate_distance_2d(axR, Z2[iB], Z2[jB], f"‖·‖iso ≈ {dB_iso:.2f}", color='seagreen')

    axR.set_title("Isomap-Einbettung (≈ intrinsische 2D-Struktur)")
    axR.set_xlabel("Komponente 1"); axR.set_ylabel("Komponente 2")
    axR.legend(loc='upper right', frameon=False)

    plt.tight_layout()
    plt.show()

    # 5) Konsole: klare Zahlen + Intrinsic-Dimension-Messung
    print("PAIR A  (rot): nah in Rohdaten, weit in Einbettung")
    print(f"  ‖·‖raw = {dA_raw:.3f}   ‖·‖iso = {dA_iso:.3f}")
    print("PAIR B (grün): weit in Rohdaten, nah in Einbettung")
    print(f"  ‖·‖raw = {dB_raw:.3f}   ‖·‖iso = {dB_iso:.3f}")

    # Neues: lokale m-Schätzung und Distanz-Konzentration
    console_explain_growth_and_concentration(X3, Z2, iA, iB, tagA="A", tagB="B")

if __name__ == "__main__":
    main()
