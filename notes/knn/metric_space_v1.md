# Metric Space

## Definition
A **metric space** is a pair \((U, D)\) where

$$
D: U \times U \to \mathbb{R}_{\ge 0}
$$

is a *distance function* satisfying, for all $x, y, z \in U$:

1. $D(x, y) \ge 0$
2. $D(x, x) = 0$
3. $x \neq y \implies D(x, y) > 0$
4. $D(x, y) = D(y, x)$
5. $D(x, z) \le D(x, y) + D(y, z)$

---

## Symbols and Components

| Symbol | Meaning | Type / Role |
|---------|----------|-------------|
| $U$ | The **set of all objects** we can measure distances between. Examples: $\mathbb{R}$, $\mathbb{R}^n$, or a set of strings, points, images, etc. | Set |
| $D$ | The **distance function**. Takes two elements of $U$ and returns a nonnegative real number. | Function $D: U \times U \to \mathbb{R}_{\ge 0}$ |
| $x, y, z$ | Arbitrary **elements (points)** in $U$. Used universally (“for all”). | Variables |
| $\mathbb{R}$ | The set of **real numbers**. | Standard symbol for real line |
| $\mathbb{R}_{\ge 0}$ | The set of **nonnegative real numbers**: $\{r \in \mathbb{R} \mid r \ge 0\}$. | Codomain of $D$ |
| $U \times U$ | The **Cartesian product** of $U$ with itself — all ordered pairs $(x, y)$ with $x, y \in U$. | Domain of $D$ |
| “for all $x, y, z \in U$” | Universal quantifier — conditions hold **for every triple of points** in $U$. | Logical quantification |
| $D(x, z) \le D(x, y) + D(y, z)$ | **Triangle inequality** — direct path no longer than detour via $y$. | Core axiom |

---

## Function Type Summary

$$
D: U \times U \longrightarrow \mathbb{R}_{\ge 0}
$$

- **Input:** Two elements $x, y \in U$  
- **Output:** A real number $r = D(x, y) \ge 0$  
- **Meaning:** “The distance between $x$ and $y$”