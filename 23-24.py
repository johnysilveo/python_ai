import random
from itertools import combinations


numbers = []
for i in range(20):
    numbers.append(random.randint(-100, 100))
product = 1
for i in range(len(numbers)):
    if i % 3 == 0:
        # print(i, numbers[i])
        product *= numbers[i]
# print(product)
negatives = []
for i in numbers:
    if i < 0:
        negatives.append(i)
sum_of_negatives = sum(negatives)
# print(sum_of_negatives)
evens = []
for i in numbers:
    if i % 2 == 0:
        evens.append(i)
sum_of_evens = sum(evens)
odds = []
for i in numbers:
    if i % 2 == 1:
        odds.append(i)
sum_of_odds = sum(odds)
min_value = min(numbers)
max_value = max(numbers)
min_index = numbers.index(min_value)
max_index = numbers.index(max_value)
start = min(min_index, max_index)
end = max(min_index, max_index)
product2 = 1
for i in range(start + 1, end):
    product2 *= numbers[i]
first_positive_index = None
last_positive_index = None
for i in range(len(numbers)):
    if numbers[i] > 0:
        first_positive_index = i
        break
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] > 0:
        last_positive_index = i
        break
sum_between_positives = 0
if first_positive_index is not None and last_positive_index is not None:
    for i in range(first_positive_index + 1, last_positive_index):
        sum_between_positives += numbers[i]
print(f"Sum of negative numbers is: {sum_of_negatives}".center(90))
print(f"Sum of even numbers is: {sum_of_evens}.".center(90))
print(f"Sum of odd numbers is: {sum_of_odds}.".center(90))
print(f"Product of numbers with index devidable by 3 is: {product}.".center(90))
print(f"Добуток елементів між мінімальним і максимальним елементом is: {product2}".center(90))
print(f"Суму елементів, що знаходяться між першим і останнім додатними елементами is: {sum_between_positives}.".center(90))


numbers = []
for i in range(50):
    numbers.append(random.randint(-100, 100))
evens = []
for i in numbers:
    if i % 2 == 0:
        evens.append(i)
odds = []
for i in numbers:
    if i % 2 == 1:
        odds.append(i)
negatives = []
for i in numbers:
    if i < 0:
        negatives.append(i)
positives = []
for i in numbers:
    if i > 0:
        positives.append(i)
print(f"Even numbers: {evens}".center(90))
print(f"Odd numbers: {odds}".center(90))
print(f"Negative numbers: {negatives}".center(90))
print(f"Positive numbers: {positives}".center(90))




text = []
print("=" * 90)
print("Enter text:".center(90))
print("Exit = exit".center(90))
while True:
    user_text = input(">" * 43 + ">")
    if user_text == "exit":
        break
    text.append(user_text)
if len(text) == 0:
    print("list is empty".center(90))
else:
    shortest_row = text[0]
    for row in text:
        if len(row) < len(shortest_row):
            shortest_row = row
    print(f"Shortest row: {shortest_row}".center(90))


text = []
print("=" * 90)
print("Enter some text".center(90))
print("To exit enter 'exit'".center(90))
while True:
    user_input = input("_" * 43 + ">").strip().lower()
    if user_input == "exit":
        break
    text.append(user_input)
what_left_text = []
print("=" * 90)
print("Enter start symbol".center(90))
start_symbol = input("_" * 43 + ">").strip().lower()
for row in text:
    if row != "" and row[0] == start_symbol:
        what_left_text.append(row)
for row in what_left_text:
    print(f"{row.capitalize()}".center(90))


text = []
print("=" * 90)
print("Enter some text".center(90))
print("To exit enter exit")
while True:
    user_text = input("_" * 43 + ">").strip().lower()
    if user_text == "exit":
        break
    text.append(user_text)
palindromes = []
for row in text:
    if row == row[::-1]:
        palindromes.append(row)
palindromes.sort(key=len, reverse=True)
for row in palindromes:
    print(f"{row.capitalize()}".center(90))


numbers = []
print("=" * 90)
print("Enter numbers to exit enter exit".center(90))
while True:
    user_text = input("_"*43+">").strip().lower()
    if user_text == "exit":
        break
    numbers.append(float(user_text))
print("Enter a target number")
target = float(input("_"*43+">"))
result= []
for size in range(1, len(numbers) + 1):
    for combination in combinations(numbers, size):
        if sum(combination) == target:
            result.append(list(combination))
print(f"Result: {result}".center(90))







