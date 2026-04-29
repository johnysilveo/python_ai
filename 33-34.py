import random


def print_results(data, *funcs):
    print("RESULTS".center(90, "-"))
    for func in funcs:
        print(f"\t{func(data)}".center(90))
    print(f"THE END".center(90,"^"))

numbers = []
for i in range(900):
    numbers.append(random.randint(-10, 100))

# Завдання 1

def find_min_in_list(number_s: list) -> str:
    return f"Minimum number in the list: {min(number_s)}"
def find_max_in_list(number_s: list) -> str:
    return f"Maximum number in the list: {max(number_s)}"

def sum_of_list(what: list) -> str:
    def calculate_sum(lst: list) -> int:
        if len(lst) == 0:
            return 0
        else:
            return lst[0] + calculate_sum(lst[1:])
    return f"Sum of list: {calculate_sum(what)}"

# Завдання 2

def prime_numbers_counter(number_s: list) -> int:
    counter = 0
    for number in number_s:
        if number < 2:
            continue
        is_prime = True
        for devider in range(2, number-1):
            if number % devider == 0:
                is_prime = False
                break
        if is_prime:
            counter += 1
    return f"Prime numbers: {counter}"

# Завдання 3

def delete_number(number_s: list, target: int) -> int:
    counter = 0
    while target in number_s:
        number_s.remove(target)
        counter += 1
    return f"Deleted number: {counter}"

# Завдання 4

def result_for_palindrome(number_s: list) -> str:
    def is_list_palindrome(number_ss: list) -> bool:
        length = len(number_ss)
        if length <= 1:
            return True
        elif number_ss[0] != number_ss[-1]:
            return False
        else:
            return is_list_palindrome(number_ss[1:-1])
    return f"Is palindrome ? {is_list_palindrome(number_s)}"

print_results(numbers,
              sum_of_list,
              find_min_in_list,
              find_max_in_list,
              prime_numbers_counter,
              lambda data: delete_number(data, 5),
              result_for_palindrome)
# Завдання 5
# Написати гру "Бики та корови". Програма "загадує" чотирицифрове число і гравець має вгадати його.
# Після введення користувачем числа програма повідомляє, скільки цифр числа вгадано (бики) і скільки
# цифр вгадано і стоїть на потрібному місці (корови). Після відгадування числа на екран необхідно
# вивести кількість зроблених користувачем спроб. У програмі необхідно використовувати рекурсію.

magic_number = str(random.randint(1000, 9999))
# print(magic_number)

def user_input():
    print("Enter 4 digit number".center(90))
    while True:
        user_choice = input("_" * 43 + ">").strip()
        if len(user_choice) != 4 or not user_choice.isdigit():
            print("WRONG!!!!!!!! Enter 4 digit number")
            continue
        return user_choice

def lets_check_user_choice(user_choice: str, magic_number: str):
    cows = 0
    bulls = 0
    for i in range(4):
        if magic_number[i] == user_choice[i]:
            cows += 1
        elif magic_number[i] in user_choice:
            bulls += 1
    return cows, bulls

def game(magic_number, attempts: int = 1):
    user_choice = user_input()
    cows, bulls = lets_check_user_choice(user_choice, magic_number)
    if cows == 4:
        print("You won!".center(90,"!"))
        print(f"Attempts made: {attempts}".center(90))
        return
    else:
        print(f"You have got {cows} cows and {bulls} bulls.".center(90))
        print("".center(90,"^"))
        game(magic_number, attempts + 1)

game(magic_number)