def min_max(lst):
    result = []
    if lst:
        minimum = lst[0]
        maximum = lst[0]
        for char in lst:
            if char < minimum:
                minimum = char
            if char > maximum:
                maximum = char
    
        result.append(minimum)
        result.append(maximum)
    return result