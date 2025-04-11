def series_sum(n):
    sum = 0
    for i in range(n):
        sum = sum + 1 / (1 + 3 * i)
    sum = round(sum, 2)
    return str(sum) + ("0" if sum == int(sum) else "")
    