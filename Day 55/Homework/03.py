def vowel_indices(word):
	vowels = 'aeiouAEIOU'
    result = []     
    for i in range(len(word)):
        if word[i] in vowels:
            result.append(i + 1)
    
    return result