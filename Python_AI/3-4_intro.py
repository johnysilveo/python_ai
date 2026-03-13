



# Task 1 (mini calc)

while True:
    number_a = float(input("Enter a number A: "))
    number_b = float(input("Enter a number B: "))
    number_c = float(input("Enter a number C: "))

    print("Enter 1 for sum\nEnter 2 for multiplication\nEnter 3 to exit")
    choice = input()
    if choice == "1":
        print(f"{number_a + number_b + number_c:.2f}")
    elif choice == "2":
        print(f"{number_a * number_b * number_c:.2f}")
    elif choice == "3":
        print('Done!')
        break
    else:
        print("Invalid choice")
        continue

# Task 2 (Rhombus area)

side_1 = int(input("Enter side 1: "))
side_2 = int(input("Enter side 2: "))
print(f"Area of rhombus is: {(side_1 * side_2)//2}")

# Task 3 (Balance)

income = float(input("Enter your income: "))
due_balance = float(input("Enter your due balance: "))
utilities = float(input("Enter your utilities: "))
print(f"You have: {income - (due_balance + utilities):.2f}$ to spare")

# Task 4 (trip cost)

distance = float(input("Enter distance to destination in miles: "))
mpg = float(input("Enter mpg of your vehicle: "))
per_gal_price = float(input("Enter price of gallon of gas: "))
gallons_used = distance / mpg
print(f"Total trip cost: {gallons_used * per_gal_price:.2f}$")

# Task 5 (ristorante)

bill = float(input("Enter total bill: "))
people = int(input("Enter number of people: "))
tip = bill * 0.15
total = bill + tip
print(f"Each person pays: ${(total / people):.2f} and total tip is {tip:.2f}")

# Task 6 (rent a car)

rent_cost = float(input("Enter daily rent cost: "))
num_of_days = int(input("Enter number of days: "))
deposit = float(input("Enter deposit: "))

rent_total = rent_cost * num_of_days
total_with_deposit = rent_total + deposit

print(f"Total due on pickup day: ${total_with_deposit:.2f}")
print(f"Deposit returned on return: ${deposit:.2f}")
print(f"Final rent cost (without deposit): ${rent_total:.2f}")
print(f"Cost per day: ${(rent_total / num_of_days):.2f}")



