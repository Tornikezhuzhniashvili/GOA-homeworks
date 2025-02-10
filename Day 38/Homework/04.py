def abbrev_name(name):
    parts = name.split()
    first_letter = parts[0][0].upper()
    second_letter = parts[1][0].upper()
    result = first_letter + "." + second_letter
    return result