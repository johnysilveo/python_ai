import time

def il_ristorante():
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
        back_option = max(menu.keys()) + 2
        while True:
            try:
                print(f"{skip_option}. Skip".center(90))
                print(f"{back_option}. Go back".center(90))
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
                    return "skip"
                elif choice == back_option:
                    return "back"
                else:
                    print(f"{'Invalid choice':^90}")
            except ValueError:
                print(f"{'Enter numbers only':^90}")

    def add_to_cart(cart, item):
        if isinstance(item, dict):
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
    time.sleep(1)

    sections = list(menus.keys())
    index = 0
    while index < len(sections):
        section = sections[index]
        menu = menus[section]
        result = choose_item(section, menu)
        if result == "back":
            if index > 0:
                index -= 1   # GO BACK!!!
            else:
                print(f"{'Already at first menu':^90}")
                time.sleep(1)
        elif result == "skip":
            index += 1
        else:
            add_to_cart(cart, result)
            index += 1

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


il_ristorante()


