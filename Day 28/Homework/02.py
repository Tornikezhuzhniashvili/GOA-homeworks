def sum_array(a):
    counter = 0
    for num in a:
        counter += num
    return counter

print(sum_array([]))
print(sum_array([1, 2, 3]))
print(sum_array([1.1, 2.2, 3.3]))
print(sum_array([4, 5, 6]))
print(sum_array(range(101)))
