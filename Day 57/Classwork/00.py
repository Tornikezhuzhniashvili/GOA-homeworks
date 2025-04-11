def lottery(s):
    result = ""
    for char in s:
        if char.isdigit() and char not in result:
            result += char
    if result:
        return result
    else:
        return "One more run!"