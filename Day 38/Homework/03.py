def digitize(n):
    result = []
    for num in str(n):
        result.append(int(num))
    result.reverse()
    return result