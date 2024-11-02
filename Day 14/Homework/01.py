numrange = int(input("Choose a range between numbers: "))
for i in range(numrange): 
    if i % 2 == 0 and i % 3 == 0:
        print(i, "These numbers are multiples of 2 and 3")
    else:
        print(i, "These numbers are not multiples of 2 and 3")


