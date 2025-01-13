def filter_list(l):
    return [item for item in l if isinstance(item, int)]


assert filter_list([1, 2, 'a', 'b']) 
assert filter_list([1, 'a', 'b', 0, 15])
assert filter_list([1, 2, 'aasf', '1', '123', 123])