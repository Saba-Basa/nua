# $\ell_p$ Norms — Product Metrics and Induced Distances

## Definition

The $\ell_p$ norm is a function that assigns a non-negative real number to each vector in $\mathbb{R}^d$:

$$
|\cdot|_p : \mathbb{R}^d \rightarrow \mathbb{R}_{\ge 0}
$$
This describes a mapping that assigns every vector in $d$-dimensional space a real number greater than or equal to zero.

For a vector $x = (x_1, x_2, \dots, x_d)$, the $\ell_p$ norm measures its size or length according to the parameter $p$.

Formally:

$$
|x|_p = \Big( \sum_{i=1}^{d} |x_i|^p \Big)^{1/p}, \qquad 1 \le p < \infty
$$
This formula takes each component's absolute value, raises it to the power $p$, sums these values, and then takes the $p$th root of that sum. The result is a single non-negative real number representing the vector’s length.

and for $p = \infty$:

$$
|x|_\infty = \max_i |x_i|
$$
The norm evaluates to the maximum absolute component of the vector, which captures the greatest deviation across all dimensions.

---

### Explanation

* $|\cdot|_p$ is the *symbol* for the $\ell_p$ norm — it is a function name.  
* The dot $\cdot$ means “insert any vector here.”  
* $\mathbb{R}^d$ is the $d$-dimensional space of vectors $(x_1, x_2, \dots, x_d)$.  
* $\mathbb{R}_{\ge 0}$ denotes the set of all non-negative real numbers — possible lengths.  
* The summation symbol $\sum_i$ means “add up all components $i = 1, \dots, d$.”  
* $|x_i|$ is the absolute value of the $i$-th coordinate (negatives don’t matter).  
* The exponent $p$ controls how strongly large components influence the result.  
* The power $1/p$ takes the $p$-th root, giving a single real number: the vector’s length.  

---

### Example

Let $x = (3, 4)$ and $p = 2$:

$$
|x|_2 = \sqrt{3^2 + 4^2} = \sqrt{25} = 5
$$
Calculating using the $p=2$ norm sums squares of each component and then takes the square root, resulting in the straight-line distance from the origin to the point $(3,4)$.

---

## Common $\ell_p$ Norms

| Name                         | Symbol         | Definition                                | Unit Ball Shape       |
| ---------------------------- | -------------- | ----------------------------------------- | --------------------- |
| **Manhattan ($L_1$)**        | $|x|_1$        | $\sum_{i=1}^{d} |x_i|$                    | Diamond               |
| **Euclidean ($L_2$)**        | $|x|_2$        | $\left(\sum_{i=1}^{d} x_i^2\right)^{1/2}$ | Circle / Sphere       |
| **Chebyshev ($L_{\infty}$)** | $|x|_{\infty}$ | $\max_{i} |x_i|$                         | Square / Cube         |

---

## Induced Distance Functions

| Metric                                   | Formula                                     | Interpretation                  |
| ---------------------------------------- | ------------------------------------------- | ------------------------------ |
| **$\ell_1$ Distance (Manhattan)**        | $D_1(x, y) = \sum_{i} |x_i - y_i|$         | Grid-based “taxicab” distance   |
| **$\ell_2$ Distance (Euclidean)**        | $D_2(x, y) = \sqrt{\sum_{i} (x_i - y_i)^2}$ | Straight-line distance          |
| **$\ell_{\infty}$ Distance (Chebyshev)** | $D_{\infty}(x, y) = \max_{i} |x_i - y_i|$  | Largest coordinate difference   |

---

## Distance Examples

### Manhattan Distance Example

Consider points $A = (1, 2)$ and $B = (4, 6)$:

$$
D_1(A, B) = |1-4| + |2-6| = 3 + 4 = 7
$$
The Manhattan distance sums the absolute differences of each coordinate, representing distance if movement is only allowed along grid lines.

---

### Euclidean Distance Example

For the same points:

$$
D_2(A, B) = \sqrt{(1-4)^2 + (2-6)^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$
The Euclidean distance measures the shortest straight-line distance between the points.

---

### Chebyshev Distance Example

Again, for points $A = (1, 2)$ and $B = (4, 6)$:

$$
D_\infty(A, B) = \max(|1-4|, |2-6|) = \max(3, 4) = 4
$$
The Chebyshev distance considers the maximum absolute difference across any coordinate, reflecting the fewest moves needed in any direction assuming diagonal movement is allowed.

---

## Properties

1. Each $|\cdot|_p$ defines a **valid norm** on $\mathbb{R}^d$.  
2. The induced distance $D_p(x, y) = |x - y|_p$ is a **metric** satisfying all metric axioms.  
3. Changing $p$ changes the geometry of the space:

   * Small $p$ → sharper, diamond-like shapes ($L_1$)  
   * Larger $p$ → rounder shapes ($L_2$)  
   * $p \to \infty$ → box-shaped geometry ($L_{\infty}$)  

4. All $\ell_p$ norms are **equivalent** in finite-dimensional spaces:
   $$
   c_1 |x|_p \le |x|_q \le c_2 |x|_p
   $$
   for constants $c_1, c_2 > 0$ depending on dimension $d$.  
This relation shows the norms behave similarly in finite dimensions and no norm can be arbitrarily large compared to another.

---

## Geometric Intuition

| $p$      | Equation of Unit Ball in $\mathbb{R}^2$     | Shape  |
| -------- | ------------------------------------------- | ------ |
| 1        | $|x_1| + |x_2| = 1$                         | Diamond |
| 2        | $x_1^2 + x_2^2 = 1$                         | Circle  |
| $\infty$ | $\max(|x_1|, |x_2|) = 1$                    | Square  |

With increasing $p$, the shape of the unit ball transitions from a diamond to a circle to a square, reflecting different “distance” concepts.

---

## Construction Context

According to Clarkson (2006), $\ell_p$ distances naturally arise as **product metrics**.  
Each coordinate space $(U_i, D_i)$ contributes its own metric, and combining them yields a single metric space:

$$
\hat{U} = U_1 \times U_2 \times \dots \times U_d, \quad
\hat{D}_p(x, y) = \Big( \sum_{i=1}^{d} D_i(x_i, y_i)^p \Big)^{1/p}.
$$
This defines the combined distance in product spaces, generalizing the $\ell_p$ norms to coordinate-wise metrics.

If $U_i = \mathbb{R}$ and $D_i(a, b) = |a - b|$, then  
$\hat{U} = \mathbb{R}^d$ and $\hat{D}_p(x, y) = |x - y|_p$.  
Hence $(\mathbb{R}^d, D_p)$ is a **metric space** for all $1 \le p \le \infty$.

---

## Example: Euclidean Distance Visualization

For $p=2$, the distance between two points $p=(p_1, p_2)$ and $q=(q_1, q_2)$ in $\mathbb{R}^2$ is

$$
d(p, q) = \sqrt{(q_1 - p_1)^2 + (q_2 - p_2)^2}.
$$

This formula computes the straight-line distance as the length of the hypotenuse of a right triangle formed by the horizontal and vertical differences.

---
