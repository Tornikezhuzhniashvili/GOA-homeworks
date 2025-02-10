def disemvowel(string_):
    vowels = "aeiouAEUIO"
    result = ""
    for char in string_:
        if char in vowels:
            continue
        result += char
    return result