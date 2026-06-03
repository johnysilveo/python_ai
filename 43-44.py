import random



list1 = []
list2 = []
list3 = []
list4 = []
for i in range(100):
    list1.append(random.randint(-100, 100))
    list2.append(random.randint(-100, 100))
    list3.append(random.randint(-100, 100))
    list4.append(random.randint(-100, 100))
list5 = list1 + list2 + list3 + list4
def task1():
    while True:
        print("1. Sort ascending")
        print("2. Sort descending")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "3":
            break
        elif choice == "2":
            list5.sort(reverse=True)
        elif choice == "1":
            list5.sort(reverse=False)
        else:
            print("Invalid choice")
            continue
        target = int(input("Enter number to find in range -100 to 100: "))
        found_index = -1
        for i in range(len(list5)):
            if list5[i] == target:
                found_index = i
                break
        if found_index != -1:
            print("Number found at index:", found_index)
        else:
            print("Number not found")
# task1()

    # Second task

def binary_search():
    temp_all_numbers = list1 + list2 + list3 + list4
    list6 = []
    for number in temp_all_numbers:
        if temp_all_numbers.count(number) == 1:
            list6.append(number)
    # print(list6)
    while True:
        print("1. Sort ascending")
        print("2. Sort descending")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "3":
            break
        elif choice == "2":
            list6.sort(reverse=True)
        elif choice == "1":
            list6.sort(reverse=False)
        else:
            print("Invalid choice")
            continue
    while True:
        print("1. Exit")
        print("2. See the list")
        print("3. Enter target number to find")
        choice = input("Enter your choice: ")
        if choice == "1":
            break
        elif choice == "2":
            print(list6)
        elif choice == "3":
            search_list6 = sorted(list6)
            target = int(input("Enter number to find in range -100 to 100: "))
            left = 0
            right = len(search_list6) - 1
            found_index = -1
            while left <= right:
                middle = (left + right) // 2
                if search_list6[middle] == target:
                    found_index = middle
                    break
                elif search_list6[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            if found_index != -1:
                print("Number found at index:", found_index)
            else:
                print("Number not found")
        else:
            print("Invalid choice")
binary_search()



