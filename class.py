## creates a class called book with attributes title, author, and pages.
## It also has a method called read that prints out the book's details.
class book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading '{self.title}' by {self.author}...")
        print(f"This book has {self.pages} pages.") 

## Inherits the book class and creates instance of the book class
## and adds a new attribute genre to the story_book class.
class story_book(book):    
    def __init__(self, title, author, pages, genre):
        super().__init__(title, author, pages)
        self.genre = genre

        print(f"Reading '{self.title}' by {self.author}...")
        print(f"This is a {self.genre} book with {self.pages} pages.")

my_book = book("Doomsday Conspiracy", "Thomas Hugh", 400)
my_book.read()
my_story_book = story_book("Charlie And the Chocolate Factory", "Neil Wilson", 350, "fiction")
my_story_book.read()


##polymorphism

class bus:
    def move(self):
        return "Bus moves by driving  "
    
class spuercar:
    def move(self):
        return "Car moves by driving in high speeds  "  
    
class bike:
    def move(self):
        return "Bike moves by pedaling  "
    
for vehicle in [bus(), spuercar(), bike()]:
    print(vehicle.move())