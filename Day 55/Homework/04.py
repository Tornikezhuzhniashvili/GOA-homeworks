def geometric_sequence_elements(a, r, n):
    sequence = []
    for i in range(n):
        term = a * (r ** i)
        sequence.append(str(term))
    return ', '.join(sequence)