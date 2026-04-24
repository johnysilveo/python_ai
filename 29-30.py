import random



numbers1,numbers2,numbers3 = [],[],[]
for number in range(random.randint(1,30)):
    numbers1.append(random.randint(1,30))
    numbers2.append(random.randint(1,30))
    numbers3.append(random.randint(1,30))
tuple_1 = tuple(numbers1)
tuple_2 = tuple(numbers2)
tuple_3 = tuple(numbers3)


result = (set(tuple_1) & set(tuple_2) & set(tuple_3))
print(f"\tЗавдання 1 \n\tМаємо три кортежі цілих чисел. Знайдіть елементи, які є у всіх кортежах.\n {result}")


result = (set(tuple_1) - set(tuple_2) - set(tuple_3))
print(f"\tЗавдання 2\n\tМаємо три кортежі цілих чисел. Знайдіть елементи, які унікальні для кожного списку. \n {result}")


result = []
for i in range(min(len(tuple_1), len(tuple_2), len(tuple_3))):
    if tuple_1[i] == tuple_2[i] == tuple_3[i]:
        result.append(tuple_1[i])
print(f"\tЗавдання 3\n\tМаємо три кортежі цілих чисел. Знайдіть елементи, які є в кожному з кортежів і знаходяться в кожному з них на тій самій позиції.\n {result}")









