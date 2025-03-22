def multi_table(number):
    table = ""
    for i in range(1, 11):
        result = i * number
        table += f"{i} * {number} = {result}\n"
    return table.strip()