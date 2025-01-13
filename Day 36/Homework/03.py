def find_short(s):
    words = s.split()
    return len(min(words, key=len))
print(find_short("bitcoin take over the world maybe who knows perhaps"))
print(find_short("bitcoin take over the world maybe who knows perhaps"))
print(find_short("bitcoin take over the world maybe who knows perhaps"))
print(find_short("i want to travel the world writing code one day"))
print(find_short("Lets all go on holiday somewhere very cold"))
print(find_short("Let's travel abroad shall we"))
            