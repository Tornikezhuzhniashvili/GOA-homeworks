def is_isogram(string):
    arr = [i for i in string.lower() if string.lower().count(i) > 1]
    if (len(arr) > 1):
        return False
    else:
        return True