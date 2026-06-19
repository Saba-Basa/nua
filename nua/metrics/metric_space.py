import math

# D:U×U→R≥0​

# metric axioms
# 1. nonnegativity        D(x, y) ≥ 0
# 2. identity             D(x, x) = 0
# 3. distinctness         x ≠ y ⇒ D(x, y) > 0
# 4. symmetry             D(x, y) = D(y, x)
# 5. triangle inequality  D(x, z) ≤ D(x, y) + D(y, z)

# Euclidean
# D(x, y) = sqrt( Σᵢ (xᵢ − yᵢ)² )


def euclide(x, y):
    # x = [1,2,3], y = [4,5,6]  →  zip(x,y) = [(1,4), (2,5), (3,6)]
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(x, y)))


# Manhattan (L₁)
# D(x, y) = Σᵢ |xᵢ − yᵢ|


def manhattan(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))


# Chebyshev (L∞)
# D(x, y) = maxᵢ |xᵢ − yᵢ|
def chebyshev(x, y):
    return max(abs(a - b) for a, b in zip(x, y))


# Hamming
# D(x, y) = number of positions where xᵢ ≠ yᵢ
def hamming(x, y):
    count = 0
    for a, b in zip(x, y):
        if a != b:
            count += 1
    return count


# Cosine angle
# D(x, y) = arccos( (x · y) / (‖x‖‖y‖) )
def cosine_angle(x, y):
    # (x · y)
    dot = sum(a * b for a, b in zip(x, y))
    # vec magnitudes (‖x‖ and ‖y‖)
    norm_x = math.sqrt(sum(a * a for a in x))
    norm_y = math.sqrt(sum(b * b for b in y))

    # zero vec
    if norm_x == 0 or norm_y == 0:
        return 0.0

    cos_theta = dot / (norm_x * norm_y)

    cos_theta = max(-1.0, min(1.0, cos_theta))
    return math.acos(cos_theta)


# Discrete
# D(x, y) = 0 if x == y else 1


def discrete(x, y):
    return 0 if x == y else 1


def check_axioms(D, x, y, z):
    if len(x) != len(y) or len(y) != len(z):
        raise ValueError("All input vectors must have the same length")

    print(f"check for: {D.__name__}")
    # 1. nonnegativity        D(x, y) ≥ 0
    nonnegativity = D(x, y) >= 0
    # 2. identity             D(x, x) = 0
    identity = D(x, x) == 0
    # 3. distinctness         x ≠ y ⇒ D(x, y) > 0
    distinctness = (x == y and D(x, y) == 0) or (x != y and D(x, y) > 0)
    # 4. symmetry             D(x, y) = D(y, x)
    symmetry = D(x, y) == D(y, x)
    # 5. triangle inequality  D(x, z) ≤ D(x, y) + D(y, z)
    triangle_inequality = D(x, z) <= D(x, y) + D(y, z)
    result = {
        "1.nonnegativity": nonnegativity,
        "2. identity": identity,
        "3. distinctness": distinctness,
        "4. symmetry": symmetry,
        "5. triangle": triangle_inequality,
    }
    result["all"] = all(result.values())
    print(result)
    return result


if __name__ == "__main__":
    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]
    check_axioms(euclide, x, y, z)
    check_axioms(manhattan, x, y, z)
    check_axioms(chebyshev, x, y, z)
    check_axioms(hamming, [1, 0, 1], [1, 1, 1], [0, 1, 1])
    check_axioms(discrete, "A", "B", "C")
