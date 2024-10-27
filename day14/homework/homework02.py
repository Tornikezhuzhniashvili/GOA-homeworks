numrange = int(input("choose range between numbrs: "))
for i in range(numrange): 
    if i % 2 == 0 and i % 3 == 0:
        print(f"{i} These numbers are multiples of 2 and 3")
    else:
        print(f"{i} This numbers are not multiples of 2 and 3")

