def longest_word(s):
    words = s.split()
    longest_word = ""
    for char in words:
        if len(char) >= len(longest_word):
            longest_word = char
    return longest_word