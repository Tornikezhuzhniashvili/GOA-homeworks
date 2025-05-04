#✅ დავალება 1:
#შექმენი class Car, რომელსაც ექნება brand, model, და year.
#და ერთ-ერთი ფუნქცია ერქმევა car_info, რომელიც დაბეჭდავს მანქანის #სრულ ინფორმაციას.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def __str__ (self):
        return f"{self.brand}, {self.model}, {self.year}"
    
c1 = Car("Subaru", "Forester", 2003)
print(c1) 