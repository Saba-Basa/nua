# $\ell_p$ Norms — Product Metrics and Induced Distances

## Definition

Let $(U_i, D_i)$ be metric spaces for $i = 1, \dots, d$.  
Their **product space** is

$$
\hat{U} = U_1 \times U_2 \times \dots \times U_d
$$

For some $p$ with $1 \le p \le \infty$, define the **product metric** as

$$
\hat{D}_p(x, y) = \Big( \sum_{i=1}^{d} D_i(x_i, y_i)^p \Big)^{1/p}
$$

If all $U_i = \mathbb{R}$ and $D_i(a, b) = |a - b|$, then $\hat{U} = \mathbb{R}^d$ and

$$
D_p(x, y) = \|x - y\|_p
$$

is the standard **$\ell_p$ distance**.

---

## Common $\ell_p$ Norms

| Name | Symbol | Definition | Unit Ball Shape |
|------|---------|-------------|----------------|
| **Manhattan ($L_1$)** | $\|x\|_1$ | $\displaystyle \sum_{i=1}^{d} |x_i|$ | Diamond |
| **Euclidean ($L_2$)** | $\|x\|_2$ | $\displaystyle \Big(\sum_{i=1}^{d} x_i^2 \Big)^{1/2}$ | Circle / Sphere |
| **Chebyshev ($L_\infty$)** | $\|x\|_\infty$ | $\displaystyle \max_i |x_i|$ | Square / Cube |

---

## Induced Distance Functions

| Metric | Formula | Interpretation |
|---------|----------|----------------|
| **$\ell_1$ Distance (Manhattan)** | $D_1(x, y) = \sum_i |x_i - y_i|$ | Grid-based “taxicab” distance |
| **$\ell_2$ Distance (Euclidean)** | $D_2(x, y) = \sqrt{\sum_i (x_i - y_i)^2}$ | Straight-line distance |
| **$\ell_\infty$ Distance (Chebyshev)** | $D_\infty(x, y) = \max_i |x_i - y_i|$ | Largest coordinate difference |

---

## Properties

1. Each $\|\cdot\|_p$ defines a **valid norm** on $\mathbb{R}^d$.  
2. The induced distance $D_p(x, y) = \|x - y\|_p$ is a **metric** satisfying all metric axioms.  
3. Changing $p$ changes the geometry of the space:
   - Small $p$ → sharper shapes ($L_1$)
   - Large $p$ → rounder shapes ($L_2$)
   - $p \to \infty$ → box-shaped geometry ($L_\infty$)
4. All $\ell_p$ norms are **equivalent** in finite-dimensional spaces:
   $$
   c_1 \|x\|_p \le \|x\|_q \le c_2 \|x\|_p
   $$
   for constants $c_1, c_2 > 0$ depending on dimension $d$.

---

## Geometric Intuition

| p | Equation of Unit Ball in $\mathbb{R}^2$ | Shape |
|---|------------------------------------------|--------|
| 1 | $\{|x_1| + |x_2| = 1\}$ | Diamond |
| 2 | $\{x_1^2 + x_2^2 = 1\}$ | Circle |
| $\infty$ | $\{\max(|x_1|, |x_2|) = 1\}$ | Square |

As $p$ increases, the $\ell_p$ ball transitions from a diamond ($p=1$) to a circle ($p=2$) to a square ($p=\infty$).  
This affects neighborhood shape, volume growth, and nearest-neighbor relationships.

---

## Construction Context

Clarkson (2006) defines these as **product metrics**, meaning $\ell_p$ distances arise naturally by combining $d$ metric coordinates $(U_i, D_i)$ into one higher-dimensional space.  
Thus, $(\mathbb{R}^d, D_p)$ is a **metric space** for all $1 \le p \le \infty$.
