import random

def generate_random_sequence(n):
    """
    Generates a random sequence of n natural numbers.
    """
    return [random.randint(1, 100) for _ in range(n)]

def generate_increasing_sequence(n):
    """
    Generates an increasing sequence of n natural numbers.
    """
    return [i+1 for i in range(n)]

def generate_decreasing_sequence(n):
    """
    Generates a decreasing sequence of n natural numbers.
    """
    return [n-i for i in range(n)]

def generate_a_shaped_sequence(n):
    """
    Generates an A-shaped sequence of n natural numbers.
    """
    center = n // 2
    spread = center
    sequence = []

    for i in range(n // 2):
        value = random.randint(center - spread, center)
        sequence.append(value)

    for i in range(n // 2, n):
        value = random.randint(center, center + spread)
        sequence.append(value)

    random.shuffle(sequence)

    return sequence

def generate_v_shaped_sequence(n):
    """
    Generates a V-shaped sequence of n natural numbers.
    """
    center = n // 2
    spread = center
    sequence = []

    for i in range(n // 2):
        value = random.randint(center + spread, center * 2)
        sequence.append(value)

    for i in range(n // 2, n):
        value = random.randint(center // 2, center - spread)
        sequence.append(value)

    random.shuffle(sequence)

    return sequence


n_values = [10, 11, 12, 13, 14, 15]

for n in n_values:
    print(f"n={n}")
    print("Random sequence:")
    for i in range(10):
        seq = generate_random_sequence(n)
        print(seq)

    print("Increasing sequence:")
    for i in range(10):
        seq = generate_increasing_sequence(n)
        print(seq)

    print("Decreasing sequence:")
    for i in range(10):
        seq = generate_decreasing_sequence(n)
        print(seq)

    print("A-shaped sequence:")
    for i in range(10):
        seq = generate_a_shaped_sequence(n)
        print(seq)

    print("V-shaped sequence:")
    for i in range(10):
        seq = generate_v_shaped_sequence(n)
        print(seq)

    print("="*20)
