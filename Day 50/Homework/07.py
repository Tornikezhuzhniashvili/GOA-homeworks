def printer_error(s):
    valid_colors = set("abcdefghijklm")
    errors = 0
    for char in s:
        if char not in valid_colors:
            errors += 1
    return f"{errors}/{len(s)}"