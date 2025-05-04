#✅ დავალება 4:
#შექმენი class Rectangle, რომელსაც ექნება width და height.
#დაუმატე ფუნქცია area, რომელიც დააბრუნებს ფართობს.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f"{self.width}, {self.height}"
    def area(self):
        return self.width * self.height
r1 = Rectangle(int(input("Enter width: ")), int(input("Enter Height")))
print(r1)
print(r1.area())