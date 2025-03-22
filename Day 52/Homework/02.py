def string_clean(s):
    text = ""
    for char in s:
        if not char.isdigit():
            text += char
    return text