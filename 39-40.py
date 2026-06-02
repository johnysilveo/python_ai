import random



numbers1 = []
for i in range(random.randint(1, 100)):
    numbers1.append(random.randint(-100, 100))

size = len(numbers1)
print(size)


average = sum(numbers1) // size
print(int(average))

one_third = len(numbers1) // 3
two_third = one_third * 2
ave = sum(numbers1) / len(numbers1)

if ave > 0:
    first_part = sorted(numbers1[:two_third])
    second_part = numbers1[two_third:][::-1]
else:
    first_part = sorted(numbers1[:one_third])
    second_part = numbers1[one_third:][::-1]

result = first_part + second_part
print(result)

# Grafes

grades = []

def add_10_grades():
    while len(grades) < 10:
        grade = int(input("Enter grade 1 to 12: "))

        if grade in range(1,13):
            grades.append(grade)
        else:
            print("Wrong grade")

def menu():
    while True:
        print("1. Show grades")
        print("2. Retake exam")
        print("3. Check scholarship")
        print("4. Sort grades")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(grades)
        elif choice == "0":
            break
        elif choice == "2":
            index = int(input("Enter index to change: "))
            new_grade = int(input("Enter new grade: "))
            if index in range(1, 11) and new_grade in range(1, 13):
                grades[index - 1] = new_grade
            else:
                print("Wrong index or wrong grade")
        elif choice == "3":
            average = sum(grades) / len(grades)
            if average >= 10.7:
                print("Scholarship approved")
            else:
                print("Scholarship denied")
        elif choice == "4":
            print("1. Sort ascending")
            print("2. Sort descending")
            sort_choice = input("Enter your choice: ")
            if sort_choice == "1":
                print(sorted(grades))
            elif sort_choice == "2":
                print(sorted(grades, reverse=True))
            else:
                print("Wrong choice")

add_10_grades()
menu()
