def fake_bin(x):
    result = ''
    for num in x:
        if int(num) < 5:
            result += '0'
        else:
            result += '1'
    return result

# Example usage:
print(fake_bin("45385593107843568"))
print(fake_bin("509321967506747"))
print(fake_bin("366058562030849490134388085"))
print(fake_bin("15889923"))
print(fake_bin("800857237867"))