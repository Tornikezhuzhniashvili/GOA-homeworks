def reverse_words(s):
    split_word = s.split(" ")[::-1]
    return " ".join(split_word)