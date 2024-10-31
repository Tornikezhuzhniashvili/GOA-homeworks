_user = input("Enter a number: ")

number = int(_user)
if number >= 100 and number % 2 == 0:
    print(str(number) + " is more than 100 but isn't even")
else:
    print(str(number) + " does not match the condition")