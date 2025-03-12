def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    return f"{max(num_list)} {min(num_list)}"