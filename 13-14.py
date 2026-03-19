import time
import math
import product


def header_start_end():
    print("=" * 90)
    print(f"{'Enter the beginning of range and the end of the range':^90}")
    print(f"{'Enter 0 0 to exit':^90}")
    print("=" * 90)
    print(f"{'Beginning of range':^90}")
    start = int(float(input("_" * 43 + ">")))
    print(f"{'End of the range':^90}")
    end = int(float(input("_" * 43 + ">")))
    if start > end:
        start, end = end, start
    return start, end


# Task 1

# running = True
# while running:
#     start, end = header_start_end()
#     if start == 0 and end == 0:
#         running = False
#     for num in range(start, end + 1):
#         if num % 7 == 0:
#             print(f"{num:^90}")

# Task 2

# running = True
# while running:
#     start, end = header_start_end()
#     if start == 0 and end == 0:
#         break
#     numero = 0
#     row = ""
#     count = 0
#     print(f"{'NUMBERS DIVISIBLE BY 7':^90}")
#     for num in range(start, end + 1):
#         if num % 5 == 0:
#             numero += 1
#         if num % 7 == 0:
#             row += f"{num:^6}"
#             count += 1
#             if count % 10 == 0:
#                 print(f"{row:^90}")
#                 row = ""
#     if row:
#         print(f"{row:^90}")
#     print("=" * 90)
#     print(f"{'Number of numbers divisible by 5 is ' + str(numero):^90}")


    # Task 3

# while True:
#     print(f"{'Enter number in range 1-100':^90}")
#     print(f"{'Exit - 101':^90}")
#     user_input = int(float(input("_" * 43 + ">")))
#     if user_input == 101:
#         break
#     if 1 <= user_input <= 100:
#         if user_input % 3 == 0 and user_input % 5 == 0:
#             print(f"{'Fizz Buzz':^90}")
#         elif user_input % 5 == 0:
#             print(f"{'Buzz':^90}")
#         elif user_input % 3 == 0:
#             print(f"{'Fizz':^90}")
#         else:
#             print(f"{user_input:^90}")
#     else:
#         print("{'ERROR':^90}")
#         print(f"{'Number must be in range 1-100':^90}")
#     time.sleep(1)

# Task 4

# running = True
# while running:
#     start, end = header_start_end()
#     if start == 0 and end == 0:
#         break
#     print(f"{'Enter step':^90}")
#     step = int(float(input("_" * 43 + ">")))
#     print(f"{'1 - Forward | 2 - Reverse':^90}")
#     choice = int(float(input("_" * 43 + ">")))
#     if choice == 1:
#         for num in range(start, end + 1, step):
#             print(f"{num:^90}")
#     elif choice == 2:
#         for num in range(end, start - 1, -step):
#             print(f"{num:^90}")

# Task 5

# while True:
#     start, end = header_start_end()
#     if start == 0 and end == 0:
#         break
#     product = 1
#     found = False
#     for num in range(start, end + 1):
#         if num % 4 == 0 and num % 6 != 0:
#             product *= num
#             found = True
#     if found:
#         print(f"{f'Product of numbers divisible by 4 and not divisible by 6 is {product}':^90}")
#         time.sleep(4)
#     else:
#         print(f"{'No such numbers':^90}")
#         time.sleep(1)

# Task 6

while True:
    print("=" * 90)
    print(f"{'Enter number A and power N':^90}")
    print(f"{'Enter 0 0 to exit':^90}")
    print("=" * 90)
    print(f"{'Enter A':^90}")
    a = int(float(input("_" * 43 + ">")))
    print(f"{'Enter N':^90}")
    n = int(float(input("_" * 43 + ">")))
    if a == 0 and n == 0:
        break
    result = 1
    for i in range(n):
        result *= a
    print(f"{f'Result is: {result}':^90}")
    time.sleep(3)
