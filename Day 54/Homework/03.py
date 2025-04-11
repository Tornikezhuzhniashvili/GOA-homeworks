def round_to_next5(n):
    if n % 5 == 0:
        return n
    return (n // 5 + 1) * 5