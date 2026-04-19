import random
import re



# numbers = []
# odd_count = 0
# even_count = 0
# print("=" * 90)
# print(f"Enter numbers and press enter. To exit enter 'exit'".center(90))
# while True:
#     user_input = input("_" * 43 + ">")
#     if user_input == "exit":
#         break
#     parts = user_input.split()
#     for item in parts:
#         try:
#             numbers.append(int(item))
#         except ValueError:
#             print(f"'{item}' is not an integer.")
# for i in numbers:
#     if i % 2 == 0:
#         even_count += 1
#     elif i % 2 == 1:
#         odd_count += 1
# print(f"Odd numbers: {odd_count}".center(90))
# print(f"Even numbers: {even_count}".center(90))


# numbers = []
# print("=" * 90)
# print(f"Enter numbers and press enter. To exit enter 'exit'".center(90))
# while True:
#     user_input = input("_" * 43 + ">")
#     if user_input == "exit":
#         break
#     parts = user_input.split()
#     for item in parts:
#         try:
#             numbers.append(int(item))
#         except ValueError:
#             print(f"'{item}' is not an integer.")
# print(f"Max number is: {max(numbers)}".center(90))
# print(f"Min number is: {min(numbers)}".center(90))


# numbers = []
# negatives_count = 0
# positives_count = 0
# zeros_count = 0
# positives = []
# negatives = []
# for i in range(100):
#     numbers.append(random.randint(-100, 100))
# for i in numbers:
#     if i > 0:
#         positives.append(i)
#     if i < 0:
#         negatives.append(i)
#     if i > 0:
#         positives_count += 1
#     elif i == 0:
#         zeros_count += 1
#     elif i < 0:
#         negatives_count += 1
# print(f"{positives_count} positive, {negatives_count} negative, zeros {zeros_count}".center(90))
# print(f"Min positive number is: {min(positives)}".center(90))
# print(f"Max negative number is: {max(negatives)}".center(90))


# numbers = []
# print("=" * 90)
# print(f"Enter numbers and press enter. To exit enter 'exit'".center(90))
# while True:
#     user_input = input("_" * 43 + ">")
#     if user_input == "exit":
#         break
#     parts = user_input.split()
#     for item in parts:
#         try:
#             numbers.append(int(item))
#         except ValueError:
#             print(f"'{item}' is not an integer.")
# print("Enter special number".center(90))
# special_number = int(input("_" * 43 + ">"))
# filtered = []
# for i in numbers:
#     if i >= special_number:
#         filtered.append(i)
# numbers = filtered
# print(f"{numbers}".center(90))



def basic_calc ():
    while True:
        print("=" * 90)
        print("Enter expression as 2+2".center(90))
        print("Available operations are ' + - * /'".center(90))
        print("To exit enter 'exit'".center(90))
        pattern = r"\s*(-?(?:\d+(?:\.\d+)?|\.\d+))\s*([+\-*/])\s*(-?(?:\d+(?:\.\d+)?|\.\d+))\s*"
        expression = input("_"*43+">").strip().lower()
        if expression == "exit":
            break
        match = re.fullmatch(pattern, expression)
        if match is None:
            print("Invalid expression".center(90))
            return
        first_number = float(match.group(1))
        operator = match.group(2)
        second_number = float(match.group(3))
        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/" and second_number != 0:
            result = first_number / second_number
        elif operator == "/" and second_number == 0:
            print("You can't divide by zero")
            return
        # return result
        print(f"{expression} = {result}".center(90))

# basic_calc()



# numbers = [-1,2,65,-54,0,32,-78,9,2,5,-1,-9,55,0]
numbers = []
print("=" * 90)
print(f"{'Enter some numbers':^90}")
print("To exit enter 'exit'".center(90))
while True:
    user_input = input("_" * 43 + ">")
    if user_input == "exit":
        break
    parts = user_input.split()
    for item in parts:
        try:
            numbers.append(int(item))
        except ValueError:
            print(f"'{item}' is not an integer.")
sorted_list = []
for i in numbers:
    if i >= 0:
        sorted_list.append(i)
sorted_list.sort()
index_sorted = 0
result = []
for i in numbers:
    if i < 0:
        result.append(i)
    else:
        result.append(sorted_list[index_sorted])
        index_sorted += 1







