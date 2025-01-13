def sum_array(a):
    return sum(a) if a else 0

print(sum_array([]))
print(sum_array([1, 2, 3]))
print(sum_array([1.1, 2.2, 3.3]))
print(sum_array([4, 5, 6]))
print(sum_array(range(101)))