#დავბალება 5 :
#მომხარებლს შეეკთეთ თუ რამდენი წლის არის მომხარებელი შემდეგ შევანახიოთ თუ ეს მომხარებელი არის 12 წელზე ზემოთ მაშინ დაგვიპრინტოს "შენ არ ხარ 12 წლის"
age = int(input("How old are you: "))

for i in range(1):
    if age > 12:
        print("Your are not 12")
    else:
        print("You are 12 or younger")