


codes = [415,808,606]
phones = [2486067,5678423, 5671509]
users = list(zip(codes, phones))


def phones_n_codes():
    while True:
        print("1. Sort by ID codes")
        print("2. Sort by phone numbers.")
        print("3. Show users")
        print("0.Exit")
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            users_sort1 = sorted(users, key=lambda user: user[0])
            #users = sorted(user, key=lambda user: user[0]) це як що не створювати новий список а фігачити основний
            for code, phone in users_sort1:
                print(f"Code: {code} phone: {phone}")
        elif choice == "2":
            users_sort2 = sorted(users, key=lambda user: user[1])
            for code, phone in users_sort2:
                print(f"Code: {code} phone: {phone}")
        elif choice == "3":
            for code, phone in users:
                print(f"Code: {code} phone: {phone}")
        else:
            print("Invalid choice")
phones_n_codes()


books = ["Dune", "1984", "It"]
years = [1965, 1949, 1986]
library = list(zip(books, years))


def books_n_years():
    while True:
        print("1. Sort books by name")
        print("2. Sort books by year.")
        print("3. Show all books")
        print("0.Exit")
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            books_sort1 = sorted(library, key=lambda book: book[0])
            #library = sorted(library, key=lambda book: book[0]) це як що не створювати новий список а фігачити основний
            for book, year in books_sort1:
                print(f"Book: {book} year: {year}")
        elif choice == "2":
            books_sort2 = sorted(library, key=lambda book: book[1])
            for book, year in books_sort2:
                print(f"Book: {book} year: {year}")
        elif choice == "3":
            for book, year in library:
                print(f"Book: {book} year: {year}")
        else:
            print("Invalid choice")
books_n_years()