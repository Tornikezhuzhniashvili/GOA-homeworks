def series_sum(n):
    sum = []
    for i in range(n):
        sum += 1 / (1 + 3 * i)
    return sum