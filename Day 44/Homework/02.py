def binary_array_to_number(arr):
    result = 0
    for i in arr:
        result = result * 2 + int(i)
    return result