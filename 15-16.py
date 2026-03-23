import time



def two_numbers():
    print(f"{'Enter first number':^90}")
    first_number = int(float(input("_"*43+">")))
    print(f"{'Enter second number':^90}")
    second_number = int(float(input("_"*43+">")))
    return first_number, second_number

def one_number():
    print("=" * 90)
    print(f"{'Enter a number':^90}")
    user_input = int(float(input("_" * 43 + ">")))
    return user_input

# Task 1

def task_1():
    sum_even = 0
    count_even = 0
    sum_odd = 0
    count_odd = 0
    mult_9 = 0
    count_mult_9 = 0
    a, b = two_numbers()
    for i in range(a, b+1):
        if i % 2 == 0:
            sum_even += i
            count_even += 1
        if i % 2 != 0:
            sum_odd += i
            count_odd += 1
        if i % 9 == 0:
            mult_9 += i
            count_mult_9 += 1
    if count_even != 0:
        avg_even = sum_even / count_even
    else:
        avg_even = 0
    if count_odd != 0:
        avg_odd = sum_odd / count_odd
    else:
        avg_odd = 0
    if mult_9 != 0:
        avg_mult9 = mult_9 / count_mult_9
    else:
        avg_mult9 = 0
    print("=" * 94)
    print(f"{'EVEN':^30}{'ODD':^30}{'MULTIPLE OF 9':^30}")
    print("-" * 94)
    print(f"|{'Sum: ' + str(sum_even):^30}|{'Sum: ' + str(sum_odd):^30}|{'Sum: ' + str(mult_9):^30}|")
    print(f"|{'Count: ' + str(count_even):^30}|{'Count: ' + str(count_odd):^30}|{'Count: ' + str(count_mult_9):^30}|")
    print(f"|{'Avg: ' + str(avg_even):^30}|{'Avg: ' + str(avg_odd):^30}|{'Avg: ' + str(avg_mult9):^30}|")
    print("-" * 94)

# task_1()

# Task 2

def task_2():
    user_input = str(input("Enter symbol: "))
    user_number = int(input("Enter number: "))
    for i in range(1,user_number+1):
        print(user_input)

# task_2()

# Task 3

def task_3():
    while True:
        print("=" * 90)
        print(f"{'To exit enter 7':^90}")
        try:
            number = float(input("_"*43+">"))
        except ValueError:
            print(f"{'Error, enter number':^90}"), time.sleep(1)
            continue
        if number == 7:
            print("Goodbye")
            break
        elif number > 0:
            print(f"{'Number is positive':^90}"),time.sleep(1)
        elif number < 0:
            print(f"{'Number is negative':^90}"),time.sleep(1)
        elif number == 0:
            print(f"{'Number is zero':^90}"),time.sleep(1)

# task_3()

# Task 4

numbers = []

def add_to_numbers(numbers, number):
        numbers.append(number)

def task_4():
    print("=" * 90)
    print(f"{'Enter numbers to finish type "done" or 7':^90}")
    print("=" * 90)
    while True:
        user_input = input("-" *43 + ">").strip().lower()
        if user_input == "done":
            print(f"{'Goodbye':^90}")
            break
        try:
            user_input = int(user_input)
        except ValueError:
            print(f"{'Please enter a number':^90}")
            continue
        if user_input == 7:
            print(f"{'Goodbye':^90}")
            break
        else:
            add_to_numbers(numbers, user_input)
    if len(numbers) > 0:
        print(f"{f'Sum of number is {sum(numbers)}':^90}")
        print(f"{f'Max number is {max(numbers)}':^90}")
        print(f"{f'Min number is {min(numbers)}':^90}")
    else:
        print(f"{'No numbers were entered':^90}")

# task_4()

# Task 5

def task_5():
    user_input = one_number()
    if user_input <= 1:
        print(f"{'Number must be grater then 1':^90}")
        return
    for i in range(2, user_input):
        if user_input % i == 0:
            print(f"{f'Number {user_input} is not prime number':^90}")
            break
    else:
        print(f"{f'Number {user_input} is prime number':^90}")

# task_5()

# Task 6

def task_6():
    user_input = one_number()
    a = 0
    b = 1
    if user_input == 0 or user_input == 1:
        print(f"{f"Number{user_input} is Fibonacci number":^90}")
        return
    while b < user_input:
        next_num = a + b
        a = b
        b = next_num
    if b == user_input:
        print(f"{f"Number ({user_input}) is Fibonacci number":^90}")
    else:
        print(f"{f"Number ({user_input}) is NOT Fibonacci number":^90}")

task_6()



