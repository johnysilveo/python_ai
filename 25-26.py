



numbers = []
count = 0
print("=" * 90)
print("Enter numbers".center(90, "-"))
print("To exit enter 'exit'".center(90, "-"))
while True:
    user_input = input("_" * 43 + ">").strip().lower()
    if user_input == "exit":
        break
    parts = user_input.split()
    for item in parts:
        try:
            numbers.append(int(item))
        except ValueError:
            print(f"'{item}' is not an integer.")
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        count += 1
print(f"Number of elements {count}".center(90, "-"))



numbers = []
print("=" * 90)
print("Enter numbers".center(90, "-"))
print("To exit enter 'exit'".center(90, "-"))
while True:
    user_input = input("_" * 43 + ">").strip().lower()
    if user_input == "exit":
        break
    parts = user_input.split()
    for item in parts:
        try:
            numbers.append(int(item))
        except ValueError:
            print(f"'{item}' is not an integer.")
print("Enter number for move".center(90, "-"))
number_n = int(input("_" * 43 + ">"))
number_n = number_n % len(numbers)
if number_n == 0:
    shifted = numbers[:]
else:
    shifted = numbers[-number_n:] + numbers[:-number_n]
print(f"Shifted list: {shifted}".center(90))
