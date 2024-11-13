#დავალება 2 :
#შექმნი სია სადაც იქნება სადაც იანქბა ციფრები რომელიც გამოიტყანს 5 სა და 3ის ჯერადევბს

number_list = [52, 85, 21, 39, 73, 65, 80, 45, 34, 25]

for num in number_list:
    if num % 5 == 0 and num % 3 == 0:
        print(num, "multiple of 3 and 5")
    elif num % 5 == 0:
        print(num, "multiple of 5")
    elif num % 3 == 0:
        print(num, "multiple of 3")
    else:
        print("this numbers is not multiple of 3 and 5")