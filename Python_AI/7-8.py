

# Task 1 (m,sm,dm)

while True:
    print(f"{'MENU':^20}")
    print("=" * 20)
    print(f"{'1. Centimeters':<15}")
    print(f"{'2. Decimeters':<15}")
    print(f"{'3. Millimeters':<15}")
    print(f"{'4. Miles':<15}")
    print(f"{'5. Exit':<15}")
    print("=" * 20)

    choice = input("Choose option: ")

    if choice == "5":
        break
    meters = float(input("Enter the number of meters: "))
    if choice == "1":
        print(f"Result: {meters * 100} cm")
    elif choice == "2":
        print(f"Result: {meters * 10} dm")
    elif choice == "3":
        print(f"Result: {meters * 1000} mm")
    elif choice == "4":
        print(f"Result: {meters * 0.000621371:.6f} miles")
    else:
        print("Invalid choice")
        continue

# Task 2 (triangle area)

base = float(input("Enter triangle base: "))
height = float(input("Enter triangle height: "))
print(f"Triangle area: {(base * height) / 2}")

# Task 3 (smash togather)

a = int(input("Enter first digit: "))
b = int(input("Enter second digit: "))
c = int(input("Enter third digit: "))
number = a * 100 + b * 10 + c
print(f"Number formed: {number}")

# Task 4 (wierd product)

number = int(input("Enter a four-digit number: "))
d1 = number // 1000
d2 = number // 100 % 10
d3 = number // 10 % 10
d4 = number % 10
print(f"Product of digits: {d1 * d2 * d3 * d4}")

# Task 5 (reflection)

number = int(input("Enter a four-digit number: "))
d1 = number // 1000
d2 = number // 100 % 10
d3 = number // 10 % 10
d4 = number % 10
reversed_number = d4 * 1000 + d3 * 100 + d2 * 10 + d1
print(f"Reversed number: {reversed_number}")

# Task 6...

num1 = int(input("Enter first three-digit number: "))
num2 = int(input("Enter second three-digit number: "))
a1 = num1 // 100
a2 = num1 // 10 % 10
a3 = num1 % 10
b1 = num2 // 100
b2 = num2 // 10 % 10
b3 = num2 % 10
result = a1*100000 + b1*10000 + a2*1000 + b2*100 + a3*10 + b3
print(f"Merged number: {result}")










