# Завдання 1


first_row = "Don't compare yourself with anyone in this world"
second_row =   "if you do so, you are insulting yourself."
name =        "Bill Gates"
def formated_text(first_row: str, second_row: str, name: str) -> str:
    return f"\n\t{first_row.center(90)}\n\t{second_row.center(90)}\n\t\t{name.center(60)}"
print(formated_text(first_row, second_row, name))
# Завдання 2


def even_numbers_in_range(a:int, b:int) -> list:
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result
print(even_numbers_in_range(2, 50))

#>>>>>>>>>>>>>>>>>>>>>>>>>>Second way<<<<<<<<<<<<<<<<<<<<<<

def even_numbers_in_range2(a:int, b:int):
    for i in range(a, b + 1):
        if i % 2 == 0:
            yield i
result = []
for number in even_numbers_in_range2(1, 50):
    result.append(number)
print(result)


# Завдання 3


def draw_square(a: int, symb: str, i: bool):
    top = "_" * a
    bottom = "-" * a
    if i == True:
        print(top)
        for row in range(a -2):
            print("|" + symb * (a - 2) + "|")
        print(bottom)
    else:
        print(top)
        for row in range(a):
            print("|" + " " * (a -2) + "|")
        print(bottom)

draw_square(10, "*", True)


# Завдання 4


def min_number(a: int, b: int,c: int, d: int, e: int):
    return min(a, b, c, d, e)
print(min_number(10, 20, 30, 40, 50))


# Завдання 5


def how_many_digits_in_number(number: int) -> int:
    number = str(number)
    return len(number)
print(how_many_digits_in_number(87654321))


# Завдання 6


def is_number_palindrome(number: int) -> bool:
    number = str(number)
    length = len(number)
    if number[0:length//2:] == number[length//2-1::-1]:
    # if number == number[::-1]:
        return True
    else:
        return False
print(is_number_palindrome(11))