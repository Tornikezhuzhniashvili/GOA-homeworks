def fake_bin(x):
    arr = []
    for num in x:
        if int(num) >= 5:
            arr.append("1")
        else:
            arr.append("0")
    return "".join(arr)