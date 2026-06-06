import os


def write_3_rows():
    print("Write 3 rows")
    row1 = input("Enter first row: ")
    row2 = input("Enter second row: ")
    row3 = input("Enter third row: ")
    with open("files/data.txt", "w") as file:
        for row in (row1, row2, row3):
            file.write(row + "\n")

#---------------------------------------

def check_file():
    answear = os.path.exists("files/data.txt")
    if answear:
        with open("files/data.txt", "r") as file:
            for index, line in enumerate(file):
                if index % 2 == 1:
                    print(line, end="")
    else:
        print("File not found")

# ---------------------------------------

def filter_lines():
    with open("files/data.txt", "r") as file_read, open("files/filtered.txt", "w") as file_write:
        for line in file_read:
            if "Python" in line:
                file_write.write(line)

# ---------------------------------------

def remove_numbers():
    numbers = "1","2","3","4","5","6","7","8","9","0"
    while True:
        print("1. Enter file name")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == "0":
            break
        elif choice == "1":
            file_name = input("Enter file name: ")
            if os.path.exists(f"files/{file_name}"):
                with open(f"files/{file_name}", "r+") as file , open("files/cleaned.txt", "w") as file_write:
                    for line in file:
                        for num in numbers:
                            if num in line:
                                line = line.replace(num, "")
                        file_write.write(line)
            else:
                print("File not found")

# ---------------------------------------

def analyze_log_file():
    word_count = {}
    with open("files/log.txt", "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    to_10_words = sorted_words[:10]
    with open("files/word_stats.txt", "w") as file_write:
        for word, count in to_10_words:
            file_write.write(f"{word} {count}\n")

# ---------------------------------------

def reversed_file():
    with open("files/data.txt", "r") as file:
        lines = file.readlines()
    lines_reversed = reversed(lines)
    with open("files/reversed.txt", "w") as file_write:
        for line in lines_reversed:
            file_write.write(line)

# ---------------------------------------

def homework_menu():
    while True:
        print("\n" + "=" * 90)
        print(f"{'47-48 HOMEWORK MENU':^90}")
        print("=" * 90)
        print(f"{'1. Task 1 - Write 3 rows to data.txt':^90}")
        print(f"{'2. Task 2 - Check data.txt and print every second line':^90}")
        print(f"{'3. Task 3 - Filter lines with Python':^90}")
        print(f"{'4. Task 4 - Remove numbers from selected file':^90}")
        print(f"{'5. Task 5 - Analyze log.txt and save top 10 words':^90}")
        print(f"{'6. Task 6 - Reverse lines from data.txt':^90}")
        print(f"{'0. Exit':^90}")
        print("=" * 90)
        choice = input("_" * 43 + "> ")
        if choice == "1":
            print(f"{'TASK 1 STARTED':^90}")
            write_3_rows()
            print(f"{'TASK 1 FINISHED':^90}")
        elif choice == "2":
            print(f"{'TASK 2 STARTED':^90}")
            check_file()
            print(f"\n{'TASK 2 FINISHED':^90}")
        elif choice == "3":
            print(f"{'TASK 3 STARTED':^90}")
            filter_lines()
            print(f"{'TASK 3 FINISHED':^90}")
        elif choice == "4":
            print(f"{'TASK 4 STARTED':^90}")
            remove_numbers()
            print(f"{'TASK 4 FINISHED':^90}")
        elif choice == "5":
            print(f"{'TASK 5 STARTED':^90}")
            analyze_log_file()
            print(f"{'TASK 5 FINISHED':^90}")
        elif choice == "6":
            print(f"{'TASK 6 STARTED':^90}")
            reversed_file()
            print(f"{'TASK 6 FINISHED':^90}")
        elif choice == "0":
            print(f"{'EXITING PROGRAM':^90}")
            break
        else:
            print(f"{'INVALID CHOICE':^90}")

homework_menu()