import pickle



def replace_python_with_java():
    with open("files/data.txt", "r") as file:
        text = file.read()
    new_text = text.replace("Python", "Java")
    with open("files/data.txt", "w") as file:
        file.write(new_text)

#----------------------------------- MARK II ---------------------------------------
def change_py(word1,word2):
    with open('python.txt','rb') as file:
        content = pickle.load(file)
        edited = content.lower().replace(word1,word2)
        with open('python.txt','wb') as file:
            pickle.dump(edited,file)
# change_py('python','java')

#----------------------------------------- COUNT --------------------------------------------------------

def count_symbols():
    with open("files/data.txt", "r") as file, open("files/char_count.txt", "w") as file2:
        for index, line in enumerate(file, start=1):
            clean_line = line.strip("\n")
            count = len(clean_line)
            file2.write(f'Number of symbols - {count} in row number {index}\n')

#----------------------------------- MARK II ---------------------------------------

def count_chars_in_lines():
    with open('data.txt', 'rb') as file:
        content = pickle.load(file)
        lines = content.splitlines()
        result = []
        for i, line in enumerate(lines, 1):
            result.append(f"Line {i}: {len(line)} characters")
    with open('char_count.txt', 'wb') as pedofile:
        pickle.dump(result, pedofile)

#----------------------------------------- COMPARE ----------------------------------------------------------

def compare_two_files():
    with open("files/old_version.txt", "r") as file, open("files/new_version.txt", "r") as file2, open ("files/differences.txt", "w") as new_file:
        lines_old = file.readlines()
        lines_new = file2.readlines()
        set_old = set(lines_old)
        set_new = set(lines_new)
        only_old = set_old - set_new
        only_new = set_new - set_old
        for line in only_old:
            new_file.write(line + "\n")
        for line in only_new:
            new_file.write(line + "\n")

#----------------------------------- MARK II ---------------------------------------

def compare(file1, file2, output_file):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        data1 = pickle.load(f1)
        data2 = pickle.load(f2)
    lines1 = set(data1.splitlines())
    lines2 = set(data2.splitlines())
    only_in_file1 = lines1 - lines2
    only_in_file2 = lines2 - lines1
    result = []
    result.append(f"Lines in {file1} but not in {file2}:")
    result.extend(only_in_file1)
    result.append(f"\nLines in {file2} but not in {file1}:")
    result.extend(only_in_file2)
    with open(output_file, 'wb') as out:
        pickle.dump('\n'.join(result), out)

#----------------------------------------- CENSOR ---------------------------------------------------

def censor():
    with open("files/source.txt", "r") as file, open("files/words.txt", "r") as file2, open("files/censored.txt", "w") as file3:
        text = file.read()
        words = file2.read().splitlines()
        for word in words:
            text = text.replace(word, "***")
        file3.write(text)

#----------------------------------- MARK II ---------------------------------------

def censor2(file1,file2,out_put_file):
    with open(file1,'rb') as file:
        content_s_raw = pickle.load(file)
        content_s = [word.strip().lower() for word in content_s_raw.split()]
    with open(file2,'rb') as file:
        content_w_raw = pickle.load(file)
        content_w = [word.strip().lower() for word in content_w_raw.split(',')]
    text = content_s_raw.lower()
    for word in content_w:
        text = text.replace(word, '***')
    with open(out_put_file,'wb') as file:
        pickle.dump(text, file)

#----------------------------------------- ORDERS -----------------------------------------------------

def add_order():
    order_number = input("Enter order number: ")
    item_name = input("Enter item name: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    order_line = f"{order_number} | {item_name} | {quantity} | {price}"
    with open("files/orders.txt","a") as order_file:
        order_file.write(order_line + "\n")

def show_orders():
    with open("files/orders.txt","r") as file:
        for line in file:
            line = line.rstrip("\n")
            print(line)

def find_order(order_number):
    with open("files/orders.txt", "r") as file:
        lines = file.readlines()
    for index, line in enumerate(lines):
        parts = line.rstrip("\n").split(" | ")
        if parts[0] == order_number:
            return index, parts, lines
    return None, None, lines

def search_order():
    order_number = input("Enter order number: ")
    index, parts, lines = find_order(order_number)
    if parts is None:
        print(f"Order with number {order_number} not found")
    else:
        print(" | ".join(parts))

def update_order():
    order_number = input("Enter order number: ")
    index, parts, lines = find_order(order_number)
    if parts is None:
        print(f"Order with number {order_number} not found")
    else:
        new_quantity = input("Enter new quantity: ")
        new_price = input("Enter new price: ")
        parts[2] = new_quantity
        parts[3] = new_price
        lines[index] = " | ".join(parts) + "\n"
        with open("files/orders.txt","w") as file:
            file.writelines(lines)

def delete_order():
    order_number = input("Enter order number: ")
    index, parts, lines = find_order(order_number)
    if parts is None:
        print(f"Order with number {order_number} not found")
    else:
        del lines[index]
        with open("files/orders.txt","w") as file:
            file.writelines(lines)
        print(f"Order with number {order_number} deleted")

def warehouse_menu():
    print("Welcome to Warehouse")
    while True:
        print("1. Add order")
        print("2. Search order")
        print("3. Update order")
        print("4. Delete order")
        print("5. Show orders")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_order()
        elif choice == "2":
            search_order()
        elif choice == "3":
            update_order()
        elif choice == "4":
            delete_order()
        elif choice == "5":
            show_orders()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

#----------------------------------- MARK II ---------------------------------------

def orders_menu():
    try:
        with open('orders.txt', 'rb') as file:
            orders = pickle.load(file)
    except (FileNotFoundError, EOFError):
        orders = {}
    while True:
        print('\n1. Add Order\n2. Show Orders\n3. Find by Number\n4. Update Order\n5. Delete Order\n6. Exit')
        choice = input('>>> ')
        if choice == '1':
            number = input('Order number: ')
            item = input('Item name: ')
            quantity = input('Quantity: ')
            price = input('Price: ')
            orders[number] = [item, quantity, price]
        elif choice == '2':
            for k, v in orders.items():
                print(k, v)
        elif choice == '3':
            number = input('Order number to find: ')
            if number in orders:
                print(orders[number])
            else:
                print('Not found')
        elif choice == '4':
            number = input('Order number to update: ')
            if number in orders:
                quantity = input('New quantity: ')
                price = input('New price: ')
                orders[number][1] = quantity
                orders[number][2] = price
            else:
                print('Not found')
        elif choice == '5':
            number = input('Order number to delete: ')
            if number in orders:
                del orders[number]
            else:
                print('Not found')
        elif choice == '6':
            with open('orders.txt', 'wb') as file:
                pickle.dump(orders, file)
            break

#----------------------------------------- STUDENTS ------------------------------------------------

def add_student():
    with open("files/students.txt","a") as file:
        name = input("Enter student's name: ")
        course = input("Enter course: ")
        avg_grade = input("Enter average grade: ")
        student = {
            "name": name,
            "course": course,
            "avg_grade": avg_grade
        }
        student_line = f"{student['name']} | {student['course']} | {student['avg_grade']}"
        file.write(student_line + "\n")

def show_students():
    with open("files/students.txt","r") as file:
        for line in file:
            print(line.rstrip("\n"))

def find_student(student_name):
    with open("files/students.txt", "r") as file:
        lines = file.readlines()
    for index, line in enumerate(lines):
        parts = line.rstrip("\n").split(" | ")
        if parts[0].lower() == student_name.lower():
            return index, parts, lines
    return None, None, lines

def search_student():
    student_name = input("Enter student's name: ")
    index, parts, lines = find_student(student_name)
    if parts is None:
        print(f"Student {student_name} not found")
    else:
        print(" | ".join(parts))

def update_student():
    student_name = input("Enter student's name: ")
    index, parts, lines = find_student(student_name.lower())
    if parts is None:
        print(f"Student {student_name} not found")
    else:
        new_course = input("Enter new course: ")
        new_avg_grade = input("Enter new average grade: ")
        parts[1] = new_course
        parts[2] = new_avg_grade
        lines[index] = " | ".join(parts) + "\n"
        with open("files/students.txt", "w") as file:
            file.writelines(lines)

def delete_student():
    student_name = input("Enter student's name: ")
    index, parts, lines = find_student(student_name.lower())
    if parts is None:
        print(f"Student {student_name} not found")
    else:
        del lines[index]
        with open("files/students.txt","w") as file:
            file.writelines(lines)
        print(f"Student {student_name} has been removed")

def academy():
    while True:
        print("Welcome to Academy")
        print("1. Add student")
        print("2. Search student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Show students")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            show_students()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

#----------------------------------- MARK II ---------------------------------------

def students_menu():
    try:
        with open('students.txt', 'rb') as file:
            students = pickle.load(file)
    except (FileNotFoundError, EOFError):
        students = {}

    while True:
        print('\n1. Add Student\n2. Show All\n3. Find by Name\n4. Update\n5. Delete\n6. Exit')
        choice = input('>>> ')

        if choice == '1':
            name = input('Name: ')
            course = input('Course: ')
            avg = input('Average grade: ')
            students[name] = [course, avg]

        elif choice == '2':
            for k, v in students.items():
                print(k, v)

        elif choice == '3':
            name = input('Student name: ')
            if name in students:
                print(students[name])
            else:
                print('Not found')

        elif choice == '4':
            name = input('Student to update: ')
            if name in students:
                course = input('New course: ')
                avg = input('New average: ')
                students[name] = [course, avg]
            else:
                print('Not found')

        elif choice == '5':
            name = input('Student to delete: ')
            if name in students:
                del students[name]
            else:
                print('Not found')

        elif choice == '6':
            with open('students.txt', 'wb') as file:
                pickle.dump(students, file)
            break

def mark_ii_menu():
    while True:
        print("\n" + "=" * 90)
        print("MARK II BONUS MENU - PICKLE VERSION".center(90))
        print("=" * 90)
        print("1. MARK II Task 1 - Replace word using pickle")
        print("2. MARK II Task 2 - Count chars using pickle")
        print("3. MARK II Task 3 - Compare files using pickle")
        print("4. MARK II Task 4 - Censor words using pickle")
        print("5. MARK II Task 5 - Orders menu using pickle")
        print("6. MARK II Task 6 - Students menu using pickle")
        print("7. Back to main menu")
        print("-" * 90)
        choice = input("Enter your choice >>> ")
        if choice == "1":
            print("\nMARK II TASK 1 STARTED".center(90, "-"))
            word1 = input("Enter word to replace: ")
            word2 = input("Enter new word: ")
            change_py(word1, word2)
            print("MARK II TASK 1 DONE".center(90, "-"))
        elif choice == "2":
            print("\nMARK II TASK 2 STARTED".center(90, "-"))
            count_chars_in_lines()
            print("MARK II TASK 2 DONE".center(90, "-"))
        elif choice == "3":
            print("\nMARK II TASK 3 STARTED".center(90, "-"))
            file1 = input("Enter first pickle file name: ")
            file2 = input("Enter second pickle file name: ")
            output_file = input("Enter output pickle file name: ")
            compare(file1, file2, output_file)
            print("MARK II TASK 3 DONE".center(90, "-"))
        elif choice == "4":
            print("\nMARK II TASK 4 STARTED".center(90, "-"))
            file1 = input("Enter source pickle file name: ")
            file2 = input("Enter words pickle file name: ")
            output_file = input("Enter output pickle file name: ")
            censor2(file1, file2, output_file)
            print("MARK II TASK 4 DONE".center(90, "-"))
        elif choice == "5":
            print("\nMARK II ORDERS MENU".center(90, "-"))
            orders_menu()
        elif choice == "6":
            print("\nMARK II STUDENTS MENU".center(90, "-"))
            students_menu()
        elif choice == "7" or choice.lower() in ("back", "b"):
            break
        else:
            print("\nInvalid choice. Try again.")

def homework_menu():
    while True:
        print("\n" + "=" * 90)
        print("FILES PART 2 HOMEWORK".center(90))
        print("=" * 90)
        print("1. Task 1  - Replace Python with Java")
        print("2. Task 2  - Count symbols in each line")
        print("3. Task 3  - Compare two files")
        print("4. Task 4  - Censor forbidden words")
        print("5. Task 5  - Orders / Warehouse menu")
        print("6. Task 6  - Students / Academy menu")
        print("7. MARK II - Pickle bonus menu")
        print("8. Exit")
        print("-" * 90)
        choice = input("Enter your choice >>> ")
        if choice == "1":
            print("\nTASK 1 STARTED".center(90, "-"))
            replace_python_with_java()
            print("TASK 1 DONE".center(90, "-"))
        elif choice == "2":
            print("\nTASK 2 STARTED".center(90, "-"))
            count_symbols()
            print("TASK 2 DONE".center(90, "-"))
        elif choice == "3":
            print("\nTASK 3 STARTED".center(90, "-"))
            compare_two_files()
            print("TASK 3 DONE".center(90, "-"))
        elif choice == "4":
            print("\nTASK 4 STARTED".center(90, "-"))
            censor()
            print("TASK 4 DONE".center(90, "-"))
        elif choice == "5":
            print("\nORDERS MENU".center(90, "-"))
            warehouse_menu()
        elif choice == "6":
            print("\nACADEMY MENU".center(90, "-"))
            academy()
        elif choice == "7":
            print("\nMARK II PICKLE BONUS MENU".center(90, "-"))
            mark_ii_menu()
        elif choice == "8" or choice.lower() in ("exit", "quit", "q"):
            print("\nGOODBYE".center(90, "="))
            break
        else:
            print("\nInvalid choice. Try again.")

homework_menu()