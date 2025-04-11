def even_or_odd(s):
    odd = 0
    even = 0
    for char in s:
        digit = int(char)
        if digit % 2 == 0:
            even += digit
        else:
            odd += digit
    if even > odd:
        return "Even is greater than Odd"
    elif odd > even:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"

