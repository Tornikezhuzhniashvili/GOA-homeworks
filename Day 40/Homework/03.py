def capitals(word):
    result = []
    for index in range(len(word)):
        if word[index].isupper():
            result.append(index)
    return result