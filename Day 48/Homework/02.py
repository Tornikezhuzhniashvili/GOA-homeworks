def fake_bin(x):
    result = ''
    for num in x:
        if int(num) < 5:
            result += '0'
        else:
            result += '1'
    return result