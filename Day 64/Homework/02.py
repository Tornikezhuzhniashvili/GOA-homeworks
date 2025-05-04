#✅ დავალება 3:
#შექმენი class Dog, რომელსაც ექნება name და age.
#და დაუმატე ფუნქცია bark, რომელიც დაბეჭდავს "Woof!".


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age}"
    def bark(self):
        print("Woof!") 
d1 = Dog("Maqsi", 0.2)
d1.bark()
print(d1)

    