



class Automobili:
    def __init__(self, model, make, year, engine_size, color, price):
        self.model = model
        self.make = make
        self.year = year
        self.engine_size = engine_size
        self.color = color
        self.price = price

    def show_info(self):
        print("Model:", self.model)
        print("Make:", self.make)
        print("Year:", self.year)
        print("Engine Size:", self.engine_size)
        print("Color:", self.color)
        print("Price:", self.price)

    def input_info(self):
        self.model = input("Please enter the model name: ")
        self.make = input("Please enter the make name: ")
        self.year = int(input("Please enter the year: "))
        self.engine_size = float(input("Please enter the engine size: "))
        self.color = input("Please enter the color: ")
        self.price = float(input("Please enter the price: "))

    def change_price(self):
        self.price = float(input("Enter a new price: "))

    def change_color(self, color):
        self.color = color

    def change_model(self, model):
        self.model = model

    def change_make(self, make):
        self.make = make

    def change_year(self, year):
        self.year = year

    def change_engine_size(self, engine_size):
        self.engine_size = engine_size

car = Automobili("Mustang GT", "Ford", 2020, 5.0, "Black", 35000)
car.show_info()
car.change_color("Red")
car.change_price()
car.show_info()

class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def show_info(self):
        print("Book title:", self.title)
        print("Year:", self.year)
        print("Publisher:", self.publisher)
        print("Genre:", self.genre)
        print("Author:", self.author)
        print("Price:", self.price)

    def input_info(self):
        self.title = input("Enter book title: ")
        self.year = int(input("Enter year: "))
        self.publisher = input("Enter publisher: ")
        self.genre = input("Enter genre: ")
        self.author = input("Enter author: ")
        self.price = float(input("Enter price: "))

    def change_title(self, title):
        self.title = title

    def change_year(self, year):
        self.year = year

    def change_publisher(self, publisher):
        self.publisher = publisher

    def change_genre(self, genre):
        self.genre = genre

    def change_author(self, author):
        self.author = author

    def change_price(self, price):
        self.price = price

book = Book("1984", 1949, "Secker & Warburg", "Dystopian", "George Orwell", 15.99)
book.show_info()
book.change_price(18.50)
book.change_genre("Dystopian Fiction")
book.show_info()

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def show_info(self):
        print("Stadium name:", self.name)
        print("Opening date:", self.opening_date)
        print("Country:", self.country)
        print("City:", self.city)
        print("Capacity:", self.capacity)

    def input_info(self):
        self.name = input("Enter stadium name: ")
        self.opening_date = input("Enter opening date: ")
        self.country = input("Enter country: ")
        self.city = input("Enter city: ")
        self.capacity = int(input("Enter capacity: "))

    def change_name(self, name):
        self.name = name

    def change_opening_date(self, opening_date):
        self.opening_date = opening_date

    def change_country(self, country):
        self.country = country

    def change_city(self, city):
        self.city = city

    def change_capacity(self, capacity):
        self.capacity = capacity

stadium = Stadium("Wembley Stadium", "2007", "England", "London", 90000)
stadium.show_info()
stadium.change_capacity(92000)
stadium.change_city("Greater London")
stadium.show_info()

