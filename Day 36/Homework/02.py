def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        return s[length // 2 - 1:length // 2 + 1]
    else:
        return s[length // 2]
    
print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("a"))