


class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is turned on.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} is turned off.")

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Power: {self.power} W")
        print(f"State: {'On' if self.is_on else 'Off'}")


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, max_beans_weight):
        super().__init__(brand, model, power)
        self.max_beans_weight = max_beans_weight

    def make_coffee(self):
        if self.is_on:
            print("Coffee is being prepared.")
        else:
            print("Turn on the coffee machine first.")

    def show_info(self):
        super().show_info()
        print(f"Maximum beans weight: {self.max_beans_weight} g")


class Blender(Device):
    def __init__(self, brand, model, power, speed_count):
        super().__init__(brand, model, power)
        self.speed_count = speed_count

    def blend(self):
        if self.is_on:
            print("The blender is working.")
        else:
            print("Turn on the blender first.")

    def show_info(self):
        super().show_info()
        print(f"Number of speeds: {self.speed_count}")


class MeatGrinder(Device):
    def __init__(self, brand, model, power, blade_count):
        super().__init__(brand, model, power)
        self.blade_count = blade_count

    def grind_meat(self):
        if self.is_on:
            print("The meat grinder is working.")
        else:
            print("Turn on the meat grinder first.")

    def show_info(self):
        super().show_info()
        print(f"Number of blades: {self.blade_count}")


coffee_machine = CoffeeMachine("DeLonghi", "Magnifica", 1450, 250)
blender = Blender("Philips", "ProBlend", 800, 5)
meat_grinder = MeatGrinder("Bosch", "MFW45020", 1600, 4)

coffee_machine.show_info()
coffee_machine.turn_on()
coffee_machine.make_coffee()

print("-" * 50)

blender.show_info()
blender.turn_on()
blender.blend()

print("-" * 50)

meat_grinder.show_info()
meat_grinder.turn_on()
meat_grinder.grind_meat()


class Airplane:
    def __init__(self,make,model,gen,typo,role,manufactor,engine_num,engine_make,
                 engine_power,jet,t_prop,payload,passengers):
        self.make = make
        self.model = model
        self.gen = gen
        self.typo = typo
        self.role = role
        self.engine_num = engine_num
        self.engine_make = engine_make
        self.engine_power = engine_power
        self.manufactor = manufactor
        self.t_prop = t_prop
        self.passengers = passengers
        self.payload = payload
        self.jet = jet

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.role == other.role
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Airplane):
            return self.passengers + other.passengers
        elif isinstance(other, int):
            return self.passengers + other
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Airplane):
            return self.passengers - other.passengers
        elif isinstance(other, int):
            return self.passengers - other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.passengers > other.passengers
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.passengers < other.passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.passengers >= other.passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.passengers <= other.passengers
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.passengers += other
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, int):
            self.passengers -= other
            return self
        return NotImplemented

    def show_info(self):
        return (f"Make: {self.make}\nModel: {self.model}\nGeneration: {self.gen}\nType: {self.typo}"
                f"\nRole: {self.role}\nNumber of engines: {self.engine_num}\nEngine make: {self.engine_make}"
                f"\nEngine power output in lbf: {self.engine_power}\nManufacture: {self.manufactor}")


class Passenger(Airplane):
    def __init__(self,make,model,gen,typo,manufactor,role,engine_num,engine_make,engine_power,
                 interior_config,num_made,crew,years_of_service,jet,t_prop,payload,passengers):
        super().__init__(make,model,gen,typo,role,manufactor,engine_num,
                         engine_make,engine_power,jet,t_prop,payload,passengers)
        self.num_made = num_made
        self.interior_config = interior_config
        self.crew = crew
        self.years_of_service = years_of_service

    def show_info(self):
        return super().show_info() + (
            f"\nNumber produced: {self.num_made}\nCrew: {self.crew}\nYears in service: {self.years_of_service}"
            f"\nInterior configuration: {self.interior_config}\nPassenger capacity: {self.passengers} people\n"
            f"Max payload: {self.payload} kg")


class Cargo(Airplane):
    def __init__(self,make,model,gen,typo,role,manufactor,engine_num,engine_make,engine_power,
                 interior_config,num_made,crew,years_of_service,jet,t_prop,payload,passengers):
        super().__init__(make,model,gen,typo,role,manufactor,engine_num,
                         engine_make,engine_power,jet,t_prop,payload,passengers)
        self.num_made = num_made
        self.interior_config = interior_config
        self.crew = crew
        self.years_of_service = years_of_service

    def show_info(self):
        return super().show_info() + (
            f"\nNumber produced: {self.num_made}\nCrew: {self.crew}\nYears in service: {self.years_of_service}"
            f"\nCargo layout: {self.interior_config}\nMax payload: {self.payload} kg")


b747 = Passenger(
    make="Boeing", role="Passenger transport", model="747-400", gen="Modern", typo="Wide-body",
    manufactor="Boeing",engine_num=4, engine_make="Pratt & Whitney PW4056", engine_power="56,000 lbf each",
    interior_config="3-class (416 pax)", num_made=694, crew=2, years_of_service="1989–2023",
    jet="Yes", t_prop="No", payload=112760, passengers=416)

b737 = Passenger(
    make="Boeing", model="737-800",role="Passenger transport", gen="Modern", typo="Narrow-body",
    manufactor="Boeing",
    engine_num=2, engine_make="CFM56-7B", engine_power="27,300 lbf each",
    interior_config="2-class (189 pax)", num_made=5000, crew=2, years_of_service="1998–present",
    jet="Yes", t_prop="No", payload=20400, passengers=189)

a380 = Passenger(
    make="Airbus", model="A380-800",role="Passenger transport", gen="Modern", typo="Superjumbo",
    manufactor="Airbus",
    engine_num=4, engine_make="Rolls-Royce Trent 900", engine_power="70,000 lbf each",
    interior_config="3-class (555 pax)", num_made=251, crew=3, years_of_service="2007–2021",
    jet="Yes", t_prop="No", payload=84000, passengers=555)

trident = Passenger(
    make="Hawker Siddeley",role="Passenger transport", model="Trident 3B", gen="Early Jet Age",
    typo="Narrow-body", manufactor="Hawker Siddeley",
    engine_num=3, engine_make="Rolls-Royce Spey", engine_power="12,250 lbf each",
    interior_config="2-class (180 pax)", num_made=117, crew=3, years_of_service="1964–1986",
    jet="Yes", t_prop="No", payload=15870, passengers=180)

an225 = Cargo(
    make="Antonov",role="Cargo transport", model="An-225 Mriya", gen="Modern", typo="Heavy lift",
    manufactor="Antonov",
    engine_num=6, engine_make="Ivchenko Progress D-18T", engine_power="51,600 lbf each",
    interior_config="Open floor cargo deck", num_made=1, crew=6, years_of_service="1988–2022",
    jet="Yes", t_prop="No", payload=250000, passengers=0)

superguppy = Cargo(
    make="Aero Spacelines",role="Cargo transport", model="Super Guppy", gen="Cold War era",
    typo="Oversized cargo", manufactor="Aero Spacelines",
    engine_num=4, engine_make="Allison T56", engine_power="4,590 shp each",
    interior_config="Cargo bubble", num_made=5, crew=4, years_of_service="1965–present",
    jet="No", t_prop="Yes", payload=24000, passengers=0)

print(b747.show_info(), "\n")
print(b737.show_info(),'\n')
print(a380.show_info(),'\n')
print(trident.show_info(),'\n')
print(an225.show_info(),'\n')
print(superguppy.show_info())


class Money:
    def __init__(self, whole_part=0, fractional_part=0, currency="USD"):
        self.currency = currency
        self.set_amount(whole_part, fractional_part)

    def set_amount(self, whole_part, fractional_part):
        total_cents = whole_part * 100 + fractional_part
        self.whole_part = total_cents // 100
        self.fractional_part = total_cents % 100

    def get_total_cents(self):
        return self.whole_part * 100 + self.fractional_part

    def show_amount(self):
        print(f"{self.whole_part}.{self.fractional_part:02d} {self.currency}")


class Product(Money):
    def __init__(self, name, whole_part, fractional_part, currency="USD"):
        super().__init__(whole_part, fractional_part, currency)
        self.name = name

    def reduce_price(self, whole_part, fractional_part=0):
        reduction_cents = whole_part * 100 + fractional_part
        current_cents = self.get_total_cents()
        if reduction_cents < 0:
            print("The reduction cannot be negative.")
            return
        if reduction_cents > current_cents:
            print("The reduction cannot be greater than the product price.")
            return
        new_price_cents = current_cents - reduction_cents
        self.set_amount(0, new_price_cents)

    def show_info(self):
        print(f"Product: {self.name}")
        print("Price: ", end="")
        self.show_amount()


product = Product("Coffee Machine", 499, 99, "USD")
product.show_info()
product.reduce_price(50, 50)
product.show_info()