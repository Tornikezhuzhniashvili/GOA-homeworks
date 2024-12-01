#დავალება 5
#შექმენით სია, იპოვეთ კონკრეტული ელემენტის რაოდენობა count მეთოდის გამოყენებით და ამოიღეთ ეს ელემენტი სიიდან remove მეთოდით. დაბეჭდეთ ელემენტის რაოდენობა და განახლებული სია.

num_list = [1, 7, 8, 7 , 9 , 15 , 23, 7]
num_to_remove = 7
count = num_list.count(num_to_remove)

for num in range(count):
    num_list.remove(num_to_remove)
print("Count of element:", count)
print("Updated list:", num_list)