def special_pythagorean_triplet(total):
    for a in range(1, total // 3):
        for b in range(a, total // 2):
            c = total - a - b
            if a * a + b * b == c * c:
                return a * b * c
    return None

print(special_pythagorean_triplet(1000))