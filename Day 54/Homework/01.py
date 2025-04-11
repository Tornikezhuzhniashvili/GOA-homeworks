def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    total = 0
    current = begin_number
    while current <= end_number:
        total = total + current
        current = current + step
    return total