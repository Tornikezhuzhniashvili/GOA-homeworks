class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def lower(self):
        return self.name.lower()
    def __str__(self):
        return f"{self.name}, {self.surname} ({self.age})"

p1 = Person("Tornike", "Zhuzhniashvili", 16)
print(p1.lower())
print(p1)

class Human:
    def __init__(self, name, surname, age, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
    def __str__(self):
        return f"{self.name}"
    def my_surname(self):
        return f"{self.surname}"
    def my_age(self):
        return f"{self.age}"
    def my_height(self):
        return f"{self.height}"
    
h1 = Human("Tornike", "Zhuzhniashvili", 16, 183)
print(h1)
print(h1.my_surname())
print(h1.my_age())
print(h1.my_height())