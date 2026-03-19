import time
import random
import math

# count = 0
# while count != 5 and count <= 10:
#     print(f"{'Hello':^90}")
#     print(f"{count:^90}")
#     count += 2
#     time.sleep(1)
# print(f"{'MULTIPLICATION TABLE':^90}")
# for i in range(1, 10):
#     row = ""
#     for j in range(1, 10):
#         row += f"{i*j:^6}"
#     print(f"{row:^90}")

# Task 1

print(f"{'Enter number:':^90}")
a = float(input("_" * 43 + ">"))

print(f"{'Enter power (0-7):':^90}")
power = int(input("_" * 43 + ">"))

if 0 <= power <= 7:
    result = math.pow(a, power)
    print(f"{'Result:':^90}")
    print(f"{result:^90g}")
else:
    print(f"{'Power must be from 0 to 7':^90}")

# Task 2
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PLEASE check option 1 :)

running = True
while running:
    print("&" * 90)
    print("^" * 90)
    print(f"{'To continue enter 1':^90}")
    cont = float(input("_" * 43 + ">"))
    if cont == 1:
        while True:
            menu = [
                "Call from Verizon to AT&T",
                "Call from AT&T to Verizon",
                "Call from T-mobile to AT&T",
                "Call from T-mobile to Verizon",
                "Call from Verizon to T-mobile",
                "Call from AT&T to T-mobile",
                "Exit"
            ]
            print("=" * 90)
            print("-" * 90)
            print(f"{'Welcome to yours best way to calculate cell service pricing':^90}")
            print(f"{'MENU':^90}")
            for i, item in enumerate(menu, 1):
                print(f"{item} ({i})".center(90))
            print(f"{'Enter your choice':^90}")
            user_choice = float(input("_" * 43 + ">"))
            if user_choice == 7:
                running = False
                break
            print(f"{'Enter price for call':^90}")
            user_price = float(input("_" * 43 + ">"))
            print(f"{'Enter amount of minutes':^90}")
            user_minutes = float(input("_" * 43 + ">"))
            multiplier = random.randint(11, 39) / 10
            result = user_price * user_minutes * multiplier
            if user_choice == 7:
                running = False
                break
            if user_choice == 1:
                num = f"{result:.2f}"
                mirror = num[::-1]
                print(f"{'Price Verizon to AT&T':^90}")
                print(f"{num + "$" + mirror:^90}")
                time.sleep(10)
            elif user_choice == 2:
                print(f"{'Price AT&T to Verizon':^90}")
                print(f"{format(result, '.2f') + '$' :^90}")
                time.sleep(2)
            elif user_choice == 3:
                print(f"{'Price T-mobile to AT&T':^90}")
                print(f"{format(result, '.2f') + '$':^90}")
                time.sleep(2)
            elif user_choice == 4:
                print(f"{'Price T-mobile to Verizon':^90}")
                print(f"{format(result, '.2f') + '$':^90}")
                time.sleep(2)
            elif user_choice == 5:
                print(f"{'Price Verizon to T-mobile':^90}")
                print(f"{format(result, '.2f') + '$':^90}")
                time.sleep(2)
            elif user_choice == 6:
                print(f"{'Price AT&T to T-mobile':^90}")
                print(f"{format(result, '.2f') + '$':^90}")
                time.sleep(2)
            else:
                print(f"{'Invalid choice':^90}")
                time.sleep(1)
    else:
        print(f"{'Invalid choice':^90}")

# Task 2 Mark2

running = True
menu = {
    1: "Call from Verizon to AT&T",
    2: "Call from AT&T to Verizon",
    3: "Call from T-mobile to AT&T",
    4: "Call from T-mobile to Verizon",
    5: "Call from Verizon to T-mobile",
    6: "Call from AT&T to T-mobile",
    7: "Exit"
}
while running:
    print("=" * 90)
    print("-" * 90)
    print(f"{'Welcome to yours best way to calculate cell service pricing':^90}")
    print(f"{'MENU':^90}")
    for i, item in menu.items():
        print(f"{item} ({i})".center(90))
    print(f"{'Enter your choice':^90}")
    try:
        user_choice = int(input("_" * 43 + ">"))
    except ValueError:
        print(f"{'Invalid input':^90}")
        time.sleep(1)
        continue
    if user_choice == 7:
        running = False
        break
    if user_choice not in menu:
        print(f"{'Invalid choice':^90}")
        time.sleep(1)
        continue
    print(f"{'Enter price for call':^90}")
    user_price = float(input("_" * 43 + ">"))
    print(f"{'Enter amount of minutes':^90}")
    user_minutes = float(input("_" * 43 + ">"))
    multiplier = random.randint(11, 39) / 10
    result = user_price * user_minutes * multiplier
    print(f"{menu[user_choice]:^90}")
    print(f"{result:.2f}$".center(90))
    time.sleep(2)


# Task 3

while True:
    print(f"{'Enter number in range 1-100':^90}")
    print(f"{'Exit - 101':^90}")
    user_input = int(float(input("_" * 43 + ">")))
    if user_input == 101:
        break
    if 1 <= user_input <= 100:
        if user_input % 3 == 0 and user_input % 5 == 0:
            print(f"{'Fizz Buzz':^90}")
        elif user_input % 5 == 0:
            print(f"{'Buzz':^90}")
        elif user_input % 3 == 0:
            print(f"{'Fizz':^90}")
        else:
            print(f"{user_input:^90}")
    else:
        print("{'ERROR':^90}")
        print(f"{'Number must be in range 1-100':^90}")
    time.sleep(1)

# Task 4

FIXED_INCOME = 200
sales_cut_un5 = 0.03
sales_cut_to1 = 0.05
sales_cut_ov1 = 0.08
managers = ["Ronny","Rocky","Zebra"]
gross_data = {}
print(f"(" + "_" * 98 + ")")
print(f"{'Welcome to pay finder and rating system!':^90}")
time.sleep(1)
for name in managers:
    print(f"{'Enter a gross amount for Mr ' + name:^90}")
    gross = float(input("_" * 43 + ">"))
    gross_data[name] = gross
salary_data = {}
for name, gross in gross_data.items():
    if gross < 500:
        salary = FIXED_INCOME + gross * sales_cut_un5
    elif 500 <= gross <= 1000:
        salary = FIXED_INCOME + gross * sales_cut_to1
    else:
        salary = FIXED_INCOME + gross * sales_cut_ov1
    salary_data[name] = salary
best_manager = max(gross_data, key=gross_data.get)
salary_data[best_manager] +=200
print("=" * 90)
print(f"{'FINAL RESULTS':^90}")
for name in managers:
    print(f"{name:<20} sales: {gross_data[name]:>10.2f}$  salary: {salary_data[name]:>10.2f}$")
print("$" * 90)
message = f"Best manager: {best_manager} +200$!!!!!!!!!!!!!!"
print(f"{message:^90}")
print("$" * 90)
time.sleep(7)

# Task 5

running = True
menu = {
    1: "To continue enter",
    2: "Exit"
}
while running:
    print("=" * 90)
    print("-" * 90)
    print(f"{'APR Calculator':^90}")
    print(f"{'MENU':^90}")
    print("-" * 90)
    for i, item in menu.items():
        print(f"{item} ({i})".center(90))
    print(f"{'Enter your choice':^90}")
    try:
        user_choice = int(input("_" * 43 + ">"))
    except ValueError:
        print(f"{'Invalid input':^90}")
        time.sleep(1)
        continue
    if user_choice == 2:
        running = False
        break
    if user_choice not in menu:
        print(f"{'Invalid choice':^90}")
        time.sleep(1)
        continue
    print(f"{'Enter total amount of the loan':^90}")
    loan_amount = float(input(f"_" * 43 + ">"))
    print(f"{'Enter term in years':^90}")
    number_years = float(input(f"_" * 43 + ">"))
    if loan_amount <= 10000 and number_years <=3:
        rate = 0.08
    elif loan_amount <= 10000 and number_years > 3:
        rate = 0.1
    elif 10001 <= loan_amount <= 50000 and number_years <= 3:
        rate = 0.12
    elif 10001 <= loan_amount <= 50000 and number_years > 3:
        rate = 0.15
    elif loan_amount > 50000:
        rate = 0.2
    total_payment = loan_amount + (loan_amount * rate)
    months = number_years * 12
    monthly_payment = total_payment / months

    print("=" * 90)
    print(f"Total loan amount {total_payment:.2f}".center(90))
    print(f"Monthly payment: {monthly_payment:.2f}".center(90))
    time.sleep(10)


# Task 6

import time
menus = {
    "Appetizers": {
        1: {"name": "Salad", "price": 5.0},
        2: {"name": "Soup", "price": 7.0},
        3: {"name": "Mozzarella sticks", "price": 8.0},
        4: {"name": "Nuggets", "price": 7.0}
    },
    "Main courses": {
        1: {"name": "Chicken", "price": 10.0},
        2: {"name": "Fish", "price": 12.0},
        3: {"name": "Beef", "price": 14.0},
        4: {"name": "Pork", "price": 9.0}
    },
    "Desserts": {
        1: {"name": "Ice cream", "price": 3.0},
        2: {"name": "Fruits", "price": 4.0},
        3: {"name": "Cheesecake", "price": 4.0},
        4: {"name": "Bueno", "price": 3.0}
    },
    "Drinks": {
        1: {"name": "Tea", "price": 2.0},
        2: {"name": "Coke", "price": 3.0},
        3: {"name": "Sprite", "price": 3.0},
        4: {"name": "Fanta", "price": 3.0}
    }
}
cart = []

def show_section(section_name, menu):

    print("_" * 90)
    print(f"{section_name:^90}")
    for i, item in menu.items():
        print(f"{i}. {item['name']} - ${item['price']:.2f}".center(90))

def choose_item(section_name, menu):
    show_section(section_name, menu)
    skip_option = max(menu.keys()) + 1
    while True:
        try:
            print(f"{skip_option}. Skip".center(90))
            print(f"{'Choose item':^90}")
            choice = int(input("_" * 43 + ">"))
            if choice in menu:
                print(f"{'Quantity':^90}")
                qty = int(input("_" * 43 + ">"))
                item = {
                    "section": section_name,
                    "name": menu[choice]["name"],
                    "price": menu[choice]["price"],
                    "qty": qty
                }
                return item
            elif choice == skip_option:
                return None
            else:
                print(f"{'Invalid choice':^90}")
        except ValueError:
            print(f"{'Enter numbers only':^90}")


def add_to_cart(cart, item):
    if item:
        cart.append(item)

def subtotal(cart):
    return sum(i["price"] * i["qty"] for i in cart)

def has_item(cart, name):
    return any(i["name"] == name for i in cart)

def apply_specials(cart):
    dessert_discount = 0
    free_items = []
    if has_item(cart, "Soup") and has_item(cart, "Fish"):
        dessert_discount = 2
    if has_item(cart, "Chicken") and has_item(cart, "Ice cream"):
        free_items.append("Tea")
    return dessert_discount, free_items

def discount_percent(subtotal_value, cart, regular):
    sections = {"Appetizers": False, "Main courses": False, "Desserts": False}
    for i in cart:
        if i["section"] in sections:
            sections[i["section"]] = True
    percent = 0

    if all(sections.values()):
        percent = 10
    if subtotal_value > 20:
        percent = max(percent, 15)
    if regular:
        percent += 5
    return percent


print("=" * 90)
print(f"{'WELCOME TO OUR RESTAURANT':^90}")
print("=" * 90)

print(f"{'DISCOUNTS':^90}")
print(f"{'10% if appetizer + main + dessert ordered':^90}")
print(f"{'15% if order exceeds $20':^90}")
print(f"{'Regular customers get extra 5%':^90}")

print(f"{'SPECIAL OFFERS':^90}")
print(f"{'Soup + Fish -> $2 dessert discount':^90}")
print(f"{'Chicken + Ice cream -> Free Tea':^90}")

print("=" * 90)

for section, menu in menus.items():
    item = choose_item(section, menu)
    add_to_cart(cart, item)
sub = subtotal(cart)
dessert_discount, free_items = apply_specials(cart)
print(f"{'Regular customer? (y/n)':^90}")
regular = input("_" * 43 + ">").lower() == "y"
disc_percent = discount_percent(sub, cart, regular)
discount_value = sub * disc_percent / 100
total_after_discount = sub - discount_value - dessert_discount
tax_rate = 0.075
tax = total_after_discount * tax_rate
print(f"{'Enter tip amount (0 if none)':^90}")
tip = float(input("_" * 43 + ">"))
final_total = total_after_discount + tax + tip
print(f"{'Preparing receipt...':^90}")
time.sleep(2)
print("=" * 90)
print(f"{'RECEIPT':^90}")

for i in cart:
    line = i["price"] * i["qty"]
    print(f"{i['name']} x{i['qty']} - ${line:.2f}".center(90))

if dessert_discount > 0:
    print(f"{'Dessert combo discount -$2.00':^90}")

for drink in free_items:
    print(f"{'Free item added: ' + drink:^90}")

print("-" * 90)
print(f"{'Subtotal: $' + format(sub, '.2f'):^90}")
print(f"{'Discount ' + str(disc_percent) + '%: -$' + format(discount_value, '.2f'):^90}")
print(f"{'Tax 7.5%: $' + format(tax, '.2f'):^90}")
print(f"{'Tip: $' + format(tip, '.2f'):^90}")

print("=" * 90)
print(f"{'FINAL TOTAL: $' + format(final_total, '.2f'):^90}")
print("=" * 90)








