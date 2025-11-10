# Metric Space — Definition and Axioms

## Definition

A metric space is a pair $(U, D)$ where

$$
D : U \times U \to \mathbb{R}_{\ge 0}
$$

is a distance function satisfying, for all $x, y, z \in U$:

1. $D(x, y) \ge 0$ — nonnegativity  
2. $D(x, x) = 0$ — identity (zero self-distance)  
3. $x \ne y \Rightarrow D(x, y) > 0$ — distinct points are apart  
4. $D(x, y) = D(y, x)$ — symmetry  
5. $D(x, z) \le D(x, y) + D(y, z)$ — triangle inequality  

---

## Symbols and Components

| Symbol | Meaning | Type / Role |
|---------|----------|-------------|
| $U$ | The set of all objects we can measure distances between. Examples: $\mathbb{R}$, $\mathbb{R}^n$, or a set of strings, points, images, etc. | Set |
| $D$ | The distance function. Takes two elements of $U$ and returns a nonnegative real number. | Function $D : U \times U \to \mathbb{R}_{\ge 0}$ |
| $x, y, z$ | Arbitrary elements (points) in $U$. Used universally (“for all”). | Variables |
| $\mathbb{R}$ | The set of real numbers. | Standard mathematical set |
| $\mathbb{R}_{\ge 0}$ | The set of nonnegative real numbers $\{r \in \mathbb{R} \mid r \ge 0\}$. | Codomain of $D$ |
| $U \times U$ | Cartesian product — all ordered pairs $(x, y)$ with $x, y \in U$. | Domain of $D$ |
| “for all $x, y, z \in U$” | Universal quantifier — conditions hold for every triple of points in $U$. | Logical quantification |
| $D(x, z) \le D(x, y) + D(y, z)$ | Triangle inequality — direct path no longer than detour via $y$. | Core axiom |

---

## Function Type Summary

$$
D : U \times U \longrightarrow \mathbb{R}_{\ge 0}
$$

Input: two elements $x, y \in U$  
Output: a real number $r = D(x, y) \ge 0$  
Meaning: “the distance between $x$ and $y$”

---

## Construction Context

Here $U$ is our set of points — for example, take $U = \mathbb{R}$, the real line.  
Then:

$$
U \times U = \{(x, y) \mid x, y \in \mathbb{R}\}
$$

This is the set of all ordered pairs of real numbers such as $(1, 3)$, $(4, 7)$, $(-2, 5)$.  
$D$ takes such a pair $(x, y)$ and returns their distance on the number line.

Example distance function:

$$
D(x, y) = |x - y|
$$

---

## Verification Examples for Each Axiom

### (1) Nonnegativity — $D(x, y) \ge 0$

Satisfying:  
$U = \mathbb{R}$, $D(x, y) = |x - y|$  
Example: $D(2, 5) = |2 - 5| = 3 \ge 0$

Violating:  
$U = \mathbb{R}$, $D(x, y) = x - y$  
Example: $D(2, 5) = 2 - 5 = -3 < 0$

---

### (2) Identity — $D(x, x) = 0$

Satisfying:  
$U = \mathbb{R}$, $D(x, y) = |x - y|$  
Example: $D(4, 4) = |4 - 4| = 0$

Violating:  
$U = \mathbb{R}$, $D(x, y) = |x - y| + 1$  
Example: $D(4, 4) = |4 - 4| + 1 = 1 \ne 0$

---

### (3) Distinctness — $x \ne y \Rightarrow D(x, y) > 0$

Satisfying:  
$U = \mathbb{R}$, $D(x, y) = |x - y|$  
Example: $D(2, 5) = |2 - 5| = 3 > 0$

Violating:  
$U = \mathbb{R}$, $D(x, y) = 0$ for all $x, y$  
Example: $D(2, 5) = 0$ despite $2 \ne 5$

---

### (4) Symmetry — $D(x, y) = D(y, x)$

Satisfying:  
$U = \mathbb{R}$, $D(x, y) = |x - y|$  
Example: $D(2, 5) = |2 - 5| = 3$, $D(5, 2) = |5 - 2| = 3$

Violating:  
$U = \mathbb{R}$, $D(x, y) = y - x$  
Example: $D(2, 5) = 3$, $D(5, 2) = -3 \ne 3$

---

### (5) Triangle Inequality — $D(x, z) \le D(x, y) + D(y, z)$

Satisfying:  
$U = \mathbb{R}$, $D(x, y) = |x - y|$  
Example: $x = 2$, $y = 4$, $z = 6$  
$D(2, 6) = 4 \le D(2, 4) + D(4, 6) = 2 + 2 = 4$

Violating:  
$U = \mathbb{R}$, $D(x, y) = (x - y)^2$  
Example: $x = 2$, $y = 3$, $z = 5$  
$D(2, 5) = 9$, $D(2, 3) + D(3, 5) = 1 + 4 = 5$  
$9 > 5 \Rightarrow$ triangle inequality violated

---

Each property (1–5) must hold simultaneously for $D$ to be a valid metric on $U$.
