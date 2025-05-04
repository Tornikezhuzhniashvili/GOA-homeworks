#✅ დავალება 2:
#შექმენი class Student, რომელსაც ექნება name, age, და grade.
#დაუმატე ფუნქცია is_passing, რომელიც დააბრუნებს True თუ grade > 5, სხვა შემთხვევაში False.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):
        return f"{self.name}, {self.age}, {self.grade}" 
    def is_passing(self):
        if self.grade > 5:
            return True
        else:
            return False

s1 = Student(input("Enter Your name: "), int(input("Enter Your Age: ")), int(input("Enter Your Grade: ")))
    
print(s1)
print(s1.is_passing())
    