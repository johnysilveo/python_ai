import random
import time



def timer(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        end_start = end-start
        print(f"Time of execution: {end_start:.8f} seconds".center(90, "*"))
        return result
    return wrapper

ls =[]
for i in range(100):
    ls.append(random.randint(1,100))

@timer
def even_list(numbers):
    ls_even = []
    for i in numbers:
        if i % 2 == 0:
            ls_even.append(i)
    return ls_even

result_even = even_list(ls)

print(f"Original list".center(90,"="))
for index, number in enumerate(sorted(ls), start=1):
    print(f"{number:4}", end="")
    if index % 10 == 0:
        print()
print(f"Even list".center(90,"="))
for index, number in enumerate(sorted(result_even), start=1):
    print(f"{number:4}", end="")
    if index % 10 == 0:
        print()
print()

@timer
def in_range(start,end):
    odd_ls = []
    for i in range(start, end + 1):
        if i % 3 == 0:
            odd_ls.append(i)
    return odd_ls

odd_ls = in_range(0,100)

print(f"Odd list".center(90,"="))
for index, number in enumerate(sorted(odd_ls,reverse=True), start=1):
    print(f"{number:4}", end="")
    if index % 10 == 0:
        print()
print()
print(f"Number of fund odd is: {len(odd_ls)}".center(90,"="))


class MessageDecorator:
    def __init__(self, user_type):
        self.user_type = user_type

    def __call__(self, func):

        def wrapper():
            message = func()
            return f"[{self.user_type}] {message}"

        return wrapper

def order_message():
    return "Ur order is accepted!"

messages = [
    MessageDecorator("ADMIN")(order_message),
    MessageDecorator("MANAGER")(order_message),
    MessageDecorator("CLIENT")(order_message)
]

for message in messages:
    print()
    print("*" *90)
    print(message().center(90,"*"))
    print("*" *90)








