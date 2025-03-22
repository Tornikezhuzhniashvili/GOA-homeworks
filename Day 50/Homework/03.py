def longest(a1, a2):
    combined = a1 + a2
    unique_letters = set(combined)
    sorted_letters = sorted(unique_letters)
    result = "".join(sorted_letters)
    return result