def disemvowel(string_):
    vowels = "aeiou"
    result = ""
    for char in string_:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            continue
        result += char
    return result