def descending_order(num):
    res = list(str(num))
    res.sort(reverse = True)
    return int(''.join(res))    