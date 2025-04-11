def calculator(x, y, op):
    if type(x) != int:
        return "unknown value"
    if type(y) != int:
        return "unknown value"
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        return x / y
    else:
        return "unknown value"