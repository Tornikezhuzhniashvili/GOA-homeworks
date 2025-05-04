numbers = [1, 2, 3, 4, 5, 6]
result = [(lambda a: a**2)(a) for a in numbers if a % 2 == 0]
print(result)