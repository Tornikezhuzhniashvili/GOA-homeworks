def elimination(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        else:
            seen.add(num)
    return None