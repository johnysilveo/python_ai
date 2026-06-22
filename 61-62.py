import math


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than zero.")
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() > other.circumference()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() < other.circumference()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.circumference() >= other.circumference()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.circumference() <= other.circumference()
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            new_radius = self.radius - value
            if new_radius <= 0:
                raise ValueError("Radius must be greater than zero.")
            return Circle(new_radius)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            new_radius = self.radius - value
            if new_radius <= 0:
                raise ValueError("Radius must be greater than zero.")
            self.radius = new_radius
            return self
        return NotImplemented

    def show_info(self):
        return (
            f"Radius: {self.radius}\n"
            f"Circumference: {self.circumference():.2f}"
        )


circle1 = Circle(10)
circle2 = Circle(15)
print("TASK 1")
print(circle1 == circle2)
print(circle1 < circle2)
circle3 = circle1 + 5
print(circle3.show_info())
circle1 += 2
print(circle1.show_info())
print("-" * 50)


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(
                self.real + other.real,
                self.imaginary + other.imaginary
            )
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(
                self.real - other.real,
                self.imaginary - other.imaginary
            )
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real = (
                self.real * other.real
                - self.imaginary * other.imaginary
            )
            imaginary = (
                self.real * other.imaginary
                + self.imaginary * other.real
            )
            return Complex(real, imaginary)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real ** 2 + other.imaginary ** 2
            if denominator == 0:
                raise ZeroDivisionError("Cannot divide by zero complex number.")
            real = (
                self.real * other.real
                + self.imaginary * other.imaginary
            ) / denominator
            imaginary = (
                self.imaginary * other.real
                - self.real * other.imaginary
            ) / denominator
            return Complex(real, imaginary)
        return NotImplemented

    def __str__(self):
        sign = "+" if self.imaginary >= 0 else "-"
        return f"{self.real:g} {sign} {abs(self.imaginary):g}i"


complex1 = Complex(4, 5)
complex2 = Complex(2, 3)

print("TASK 2")
print(f"First number: {complex1}")
print(f"Second number: {complex2}")
print(f"Addition: {complex1 + complex2}")
print(f"Subtraction: {complex1 - complex2}")
print(f"Multiplication: {complex1 * complex2}")
print(f"Division: {complex1 / complex2}")
print("-" * 50)


class Airplane:
    def __init__(
        self,
        make,
        model,
        airplane_type,
        max_passengers,
        passengers=0
    ):
        if max_passengers < 0:
            raise ValueError("Maximum passenger capacity cannot be negative.")
        if passengers < 0 or passengers > max_passengers:
            raise ValueError("Passenger count must be between 0 and maximum capacity.")
        self.make = make
        self.model = model
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.passengers = passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.airplane_type == other.airplane_type
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            new_passenger_count = self.passengers + value
            if new_passenger_count > self.max_passengers:
                raise ValueError("Passenger count cannot exceed maximum capacity.")
            return Airplane(
                self.make,
                self.model,
                self.airplane_type,
                self.max_passengers,
                new_passenger_count
            )
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, int):
            new_passenger_count = self.passengers - value
            if new_passenger_count < 0:
                raise ValueError("Passenger count cannot be negative.")
            return Airplane(
                self.make,
                self.model,
                self.airplane_type,
                self.max_passengers,
                new_passenger_count
            )
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, int):
            new_passenger_count = self.passengers + value
            if new_passenger_count > self.max_passengers:
                raise ValueError("Passenger count cannot exceed maximum capacity.")
            self.passengers = new_passenger_count
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, int):
            new_passenger_count = self.passengers - value
            if new_passenger_count < 0:
                raise ValueError("Passenger count cannot be negative.")
            self.passengers = new_passenger_count
            return self
        return NotImplemented

    def show_info(self):
        return (
            f"Make: {self.make}\n"
            f"Model: {self.model}\n"
            f"Type: {self.airplane_type}\n"
            f"Passengers: {self.passengers}\n"
            f"Maximum passengers: {self.max_passengers}"
        )


airplane1 = Airplane(
    make="Boeing",
    model="737-800",
    airplane_type="Narrow-body",
    max_passengers=189,
    passengers=150
)

airplane2 = Airplane(
    make="Airbus",
    model="A320",
    airplane_type="Narrow-body",
    max_passengers=180,
    passengers=140
)

print("TASK 3")
print(airplane1 == airplane2)
print(airplane1 > airplane2)
airplane3 = airplane1 + 20
print(airplane3.show_info())
airplane1 += 10
airplane1 -= 5
print(airplane1.show_info())
print("-" * 50)


class Flat:
    def __init__(self, area, rooms, bathrooms, price):
        self.area = area
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.area != other.area
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price
        return NotImplemented

    def show_info(self):
        return (
            f"Area: {self.area} sq ft\n"
            f"Rooms: {self.rooms}\n"
            f"Bathrooms: {self.bathrooms}\n"
            f"Price: ${self.price:,.2f}"
        )


flat1 = Flat(
    area=1200,
    rooms=3,
    bathrooms=2,
    price=300000
)

flat2 = Flat(
    area=1200,
    rooms=4,
    bathrooms=3,
    price=350000
)

print("TASK 4")
print(flat1 == flat2)
print(flat1 != flat2)
print(flat1 < flat2)
print(flat1 > flat2)
print(flat1.show_info())
print()
print(flat2.show_info())