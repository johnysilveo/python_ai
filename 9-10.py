import math

# math.pow(2,3

# Task 1

# while True:
#     print(f"{'MENU':^90}")
#     print("=" * 90)
#     print(f"{'RULES':^90}")
#     print("-" * 90)
#     print(f"{'1':^90}")
#     print(f"{'You may choose in between of multiplication (1) and (2) division. To leave choose (3)':^90} ")
#     print(f"{'2':^90}")
#     print(f"{'You will enter 3 numbers':^90}")
#     print(f"{'Enter your choice:':^90}")
#     user_input = int(input("_" * 43 + ">"))
#     if user_input == 1:
#         print(f"{'Enter number 1':^90}")
#         a = float(input("_" * 43 + ">"))
#         print(f"{'Enter number 2':^90}")
#         b = float(input("_" * 43 + ">"))
#         print(f"{'Enter number 3':^90}")
#         c = float(input("_" * 43 + ">"))
#         result = a*b*c
#         print(f"{'RESULT':^90}")
#         print("&" * 90)
#         print(f" {f'{a:g} * {b:g} * {c:g} = {result:g}':^90}")
#         print("&" * 90)
#     elif user_input == 2:
#         print(f"{'Enter number 1':^90}")
#         a = float(input("_" * 43 + ">"))
#         print(f"{'Enter number 2':^90}")
#         b = float(input("_" * 43 + ">"))
#         print(f"{'Enter number 3':^90}")
#         c = float(input("_" * 43 + ">"))
#         result = a/b/c
#         print(f"{'RESULT':^90}")
#         print("&" * 90)
#         print(f" {f'{a:g} * {b:g} * {c:g} = {result:g}':^90}")
#         print("&" * 90)
#     elif user_input == 3:
#         print(f"{'GOODBYE':^90}")
#         break
#     else:
#         print(f"{'Invalid input':^90}")
# Task 2, 3

# exit_program = False
# while not exit_program:
#     print(f"{'MENU':^90}")
#     print("=" * 90)
#     print(f"{'Enter (1) for MAX':^90} ")
#     print(f"{'Enter (2) for MIN':^90}")
#     print(f"{'Enter (3) for AVG':^90}")
#     print(f"{'Enter your choice:':^90}")
#     print(f"{'Exit (4)':^90}")
#     user_input = int(input("_" * 43 + ">"))
#     if user_input == 1:
#         print(f"{'Enter number 1':^90}")
#         a = float(input("_" * 43 + ">"))
#         print(f"{'Enter number 2':^90}")
#         b = float(input("_" * 43 + ">"))
#         print(f"{'Enter number 3':^90}")
#         c = float(input("_" * 43 + ">"))
#         result = max(a,b,c)
#         print(f"{'RESULT':^90}")
#         print("&" * 90)
#         print(f"{f'MAX out of {a:g} * {b:g} * {c:g} is {result:g}':^90}")
#         print("&" * 90)
#     elif user_input == 2:
#         print(f"{'Enter number 1':^90}")
#         a = float(input("_" * 43 + ">"))
#         print(f"{'Enter number 2':^90}")
#         b = float(input("_" * 43 + ">"))
#         print(f"{'Enter number 3':^90}")
#         c = float(input("_" * 43 + ">"))
#         result = min(a,b,c)
#         print(f"{'RESULT':^90}")
#         print("&" * 90)
#         print(f"{f'MIN out of {a:g} * {b:g} * {c:g} is {result:g}':^90}")
#         print("&" * 90)
#     elif user_input == 3:
#         print(f"{'Enter number 1':^90}")
#         a = float(input("_" * 43 + ">"))
#         print(f"{'Enter number 2':^90}")
#         b = float(input("_" * 43 + ">"))
#         print(f"{'Enter number 3':^90}")
#         c = float(input("_" * 43 + ">"))
#         result = (a+b+c)/3
#         print(f"{'RESULT':^90}")
#         print("&" * 90)
#         print(f"{f'AVG of {a:g} * {b:g} * {c:g} is {result:g}':^90}")
#         print("&" * 90)
#     elif user_input == 4:
#         print(f"{'GOODBYE':^90}")
#         break
#     else:
#         print(f"{'Invalid input':^90}")
#         continue
#     while True:
#         print(f"{'Please rate your experience 1-5 stars':^90}")
#         print("=" * 90)
#         user_input = int(input("_" * 43 + ">"))
#         if user_input == 1:
#             print("=" * 90)
#             print(f"{'Very bad':^90}")
#             exit_program = True
#             break
#         elif user_input == 2:
#             print("=" * 90)
#             print(f"{'Bad':^90}")
#             exit_program = True
#             break
#         elif user_input == 3:
#             print("=" * 90)
#             print(f"{'Acceptable':^90}")
#             exit_program = True
#             break
#         elif user_input == 4:
#             print("=" * 90)
#             print(f"{'Good':^90}")
#             exit_program = True
#             break
#         elif user_input == 5:
#             print("=" * 90)
#             print(f"{'Excellent!!!':^90}")
#             exit_program = True
#             break
#         else:
#             print(f"{'Invalid input':^90}")
#             print("=" * 90)
#             continue

# Task 4

# import time
#
# while True:
#     print(f"{'MENU':^90}")
#     print("=" * 90)
#     print(f"{'Enter (1) for miles':^90}")
#     print(f"{'Enter (2) for inches':^90}")
#     print(f"{'Enter (3) for yards':^90}")
#     print(f"{'Enter (4) for miles, inches, yards':^90}")
#     print(f"{'Enter (5) for kilometers and centimeters':^90}")
#     print(f"{'Enter (6) for exit':^90}")
#     print(f"{'Enter your choice:':^90}")
#     user_input = int(input("_" * 43 + ">"))
#     if user_input == 6:
#         break
#     print(f"{'Enter number of meters:':^90}")
#     a = float(input("_" * 43 + ">"))
#     if user_input == 1:
#         result = a * 0.000621371
#         print(f"{f'{a:g} meters = {result:g} miles':^90}")
#     elif user_input == 2:
#         result = a * 39.3701
#         print(f"{f'{a:g} meters = {result:g} inches':^90}")
#     elif user_input == 3:
#         result = a * 1.09361
#         print(f"{f'{a:g} meters = {result:g} yards':^90}")
#     elif user_input == 4:
#         miles = a * 0.000621371
#         inches = a * 39.3701
#         yards = a * 1.09361
#         print(f"{f'{a:g} meters = {miles:g} miles, {inches:g} inches, {yards:g} yards':^90}")
#     elif user_input == 5:
#         kilometers = a * 0.001
#         centimeters = a * 100
#         print(f"{f'{a:g} meters = {kilometers:g} km and {centimeters:g} cm':^90}")
#     else:
#         print(f"{'Invalid input!':^90}")
#     time.sleep(5)


# Task 5

# import time
#
# while True:
#     print(f"{'MENU':^90}")
#     print("=" * 90)
#     print(f"{'Enter (1) for ADDITION':^90}")
#     print(f"{'Enter (2) for SUBTRACTION':^90}")
#     print(f"{'Enter (3) for MULTIPLICATION':^90}")
#     print(f"{'Enter (4) for DIVISION':^90}")
#     print(f"{'Enter (5) for REMAINDER':^90}")
#     print(f"{'Enter (6) for POWER':^90}")
#     print(f"{'Exit (7)':^90}")
#     print(f"{'Enter your choice:':^90}")
#     user_input = int(input("_" * 43 + ">"))
#     if user_input in [1,2,3,4,5,6]:
#         print(f"{'Enter first number':^90}")
#         a = float(input("_" * 43 + ">"))
#         print(f"{'Enter second number':^90}")
#         b = float(input("_" * 43 + ">"))
#         if user_input == 1:
#             result = a + b
#             operation = "+"
#         elif user_input == 2:
#             result = a - b
#             operation = "-"
#         elif user_input == 3:
#             result = a * b
#             operation = "*"
#         elif user_input == 4:
#             result = a / b
#             operation = "/"
#         elif user_input == 5:
#             result = a % b
#             operation = "%"
#         elif user_input == 6:
#             result = a ** b
#             operation = "**"
#         print(f"{'RESULT':^90}")
#         print("&" * 90)
#         print(f"{f'{a:g} {operation} {b:g} = {result:g}':^90}")
#         print("&" * 90)
#         time.sleep(5)
#     elif user_input == 7:
#         print(f"{'GOODBYE':^90}")
#         break
#     else:
#         print(f"{'Invalid input':^90}")
#         continue

# Task 6
import time

while True:
    print(f"{'MENU':^90}")
    print("=" * 90)
    print(f"{'Enter a three-digit number':^90}")
    print(f"{'Enter (0) to exit':^90}")
    try:
        number = int(input("_" * 43 + ">"))
    except ValueError:
        print(f"{'Invalid input! Enter a number.':^90}")
        time.sleep(2)
        continue
    if number == 0:
        print(f"{'GOODBYE':^90}")
        time.sleep(2)
        break
    if 100 <= abs(number) <= 999:
        a = abs(number) // 100
        b = abs(number) // 10 % 10
        c = abs(number) % 10
        print("=" * 90)
        if a == b == c:
            print(f"{'All number are the same':^90}")
            time.sleep(3)
        else:
            print(f"{'All numbers are different':^90}")
            time.sleep(3)
        print("=" * 90)
    else:
        print(f"{'This is not three-digit number!':^90}")
        time.sleep(2)





