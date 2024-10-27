birth_year = int(input("მიუთითეთ თვენი დავადების წელი: "))
current_year = 2024
age = current_year - birth_year
print(birth_year, "თქვენ ბრძანდებით", age, "წლის")

print("---------------------------------------")

length = int(input("მიუთითეთ სიგრძე: "))
width = int(input("მიუთითეთ სიგანე: "))
area = length * width
perimeter = 2 * (length + width)
print("ფართობი არის", area, "პერიმეტრი არის", perimeter)

print("----------------------------------")

kilometer = float(input("მიუთითეთ მანძილი სახლიდან სკოლამდე: "))
meters = kilometer * 1000
centimeters = kilometer * 10000
millimeters = kilometer * 100000
print("მანძილი მეტრებში არის", meters)
print("მანძილი სანტიმეტრებში არის", centimeters)
print("მანძილი მილიმეტრებში არის", millimeters)

name = input("თქვენი სახელი და გვარი: ")
parent_name = input("მშობლის სახელი და გვარი: ")
fav_color = input("თქვენი საყვარელი ფერი: ")
fav_car = input("საყვარელი მანქანა: ")
hobby1 = input("Top 1 ჰობი: ")
hobby2 = input("Top 2 ჰობი: ")
hobby3 = input("Top 3 ჰობი: ")
print("თქვენი სახელი", name, "მშობლის სახელი", parent_name, "საყვარელი ფერი", fav_color, "ფავორიტი მანქანა", fav_car, "Top 1 ჰობი", hobby1, "Top 2 ჰობი", hobby2, "Top 3 ჰობი", hobby3)