#✅ დავალება 5:
#შექმენი class Book, რომელსაც ექნება title, author, და year.
#დაუმატე ფუნქცია info, რომელიც დაბეჭდავს მაგ წიგნის დეტალებს – Title, Author, Year

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"
b1 = Book("შეცდომა", "ნათია ჯაგოდნიშვილი", 2022)
print(b1)