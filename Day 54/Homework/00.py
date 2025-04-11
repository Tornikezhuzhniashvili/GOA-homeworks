def sort_by_length(arr):
    result = arr[:]

    for i in range(len(result)):
        for char in range(len(result) - 1):
            if len(result[char]) > len(result[char + 1]):
                temp = result[char]
                result[char] = result[char + 1]
                result[char + 1] = temp
    return result
        