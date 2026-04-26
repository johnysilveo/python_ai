# Створіть програму, що містить інформацію про відомих баскетболістів.
# Збережіть ПІБ та зріст кожного баскетболіста.
# Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані.
# Використовуйте словник для збереження інформації.

basketball_players = {
    "Michael Jordan": 198,
    "LeBron James": 206,
    "Kobe Bryant": 198
}
def user_input():
    print("Please enter name of player".center(90))
    user_input_name = input("_"*43+">").strip()
    print("Please enter height of player".center(90))
    user_input_height = int(input("_"*43+">"))
    return {user_input_name: user_input_height}

def add_players(players):
    new_player = user_input()
    players.update(new_player)

def remove_players(players):
    print("Please enter name of player to be removed".center(90))
    name = input("_" * 43 + ">")
    removed = players.pop(name, None)
    if removed is None:
        print("No such player")
    else:
        print(f"{name} was removed")

def find_player(players):
    print("Please enter name of player".center(90))
    name = input("_" * 43 + ">").strip()
    found = players.get(name)
    if found is None:
        print("No such player")
    else:
        print(f"{name} was found. Height: {found}")

def change_player(players):
    print("Please enter name of player".center(90))
    name = input("_" * 43 + ">").strip()
    if name in players:
        print(f"{name} will be changed")
        players.pop(name)
        new_data = user_input()
        players.update(new_data)
    else:
        print("No such player")

def menu_print():
    print("Welcome to Basketball Player.".center(90, "-"))
    print("Choose any option".center(90))
    print("To add player enter '1'".center(90))
    print("To remove player enter '2'".center(90))
    print("To find player enter '3'".center(90))
    print("T change player enter '4'".center(90))
    print("To see the whole list enter '5'".center(90))
    print("To quit enter 'exit'".center(90))
def menu_input():
    menu_print()
    while True:
        choise = input("Choose option: " + "_" * 20 + ">").lower().strip()
        if choise == "exit":
            break
        elif choise == "1":
            add_players(basketball_players)
        elif choise == "2":
            remove_players(basketball_players)
        elif choise == "3":
            find_player(basketball_players)
        elif choise == "4":
            change_player(basketball_players)
        elif choise == "5":
            print(basketball_players)
        else:
            print("Wrong option")

# menu_input()

# Створіть програму «Англо-французький словник».
# Збережіть слово англійською та його переклад на французьку.
# Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані.
# Використовуйте словник для збереження інформації.

english_french = {
    "hello": "bonjour",
    "cat": "chat",
    "dog": "chien"
}

def user_input_word():
    print("Please enter english word".center(90))
    user_input_english = input("_"*43+">").strip().lower()
    print("Please enter french word".center(90))
    user_input_french = input("_"*43+">").strip().lower()
    return {user_input_english: user_input_french}

def add_word(words):
    new_word = user_input_word()
    words.update(new_word)

def remove_word(words):
    print("Please enter word to be removed".center(90))
    word = input("_" * 43 + ">").strip().lower()
    removed = words.pop(word, None)
    if removed is None:
        print("No such word")
    else:
        print(f"{word.capitalize()} was removed")

def find_word(words):
    print("Please enter a word".center(90))
    word = input("_" * 43 + ">").strip().lower()
    found = words.get(word)
    if found is None:
        print("No such word")
    else:
        print(f"{word.capitalize()} was found. in french: {found.capitalize()}".center(90))

def change_word(words):
    print("Please enter a word to change".center(90))
    word = input("_" * 43 + ">").strip().lower()
    if word in words:
        print(f"{word.capitalize()} will be changed".center(90))
        words.pop(word)
        new_data = user_input_word()
        words.update(new_data)
    else:
        print("No such word")

def menu_print_word():
    print("Welcome to English to French dictionary.".center(90, "-"))
    print("Choose any option".center(90))
    print("To add a word enter '1'".center(90))
    print("To remove a word enter '2'".center(90))
    print("To find a word enter '3'".center(90))
    print("To change a word enter '4'".center(90))
    print("To see the whole dictionary enter '5'".center(90))
    print("To quit enter 'exit'".center(90))
def menu_input_word():
    menu_print_word()
    while True:
        choice = input("_" * 26 + " Choose option" +  "__>").lower().strip()
        if choice == "exit":
            break
        elif choice == "1":
            add_word(english_french)
        elif choice == "2":
            remove_word(english_french)
        elif choice == "3":
            find_word(english_french)
        elif choice == "4":
            change_word(english_french)
        elif choice == "5":
            for english, french in english_french.items():
                print(f"{english.capitalize()} -> {french.capitalize()}")
        else:
            print("Wrong option")

# menu_input_word()

import time


# Створіть програму «Фірма», яка зберігає інформацію про працівників:
# ПІБ, телефон, корпоративний email, назва посади, номер кабінету, Skype.
# Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані.
# Використовуйте словник для збереження інформації.

company = {
    "John Smith": {
        "phone": "808-111-2222",
        "email": "john.smith@company.com",
        "position": "Manager",
        "office": "203",
        "skype": "john.smith"
    },
    "Anna Brown": {
        "phone": "808-222-3333",
        "email": "anna.brown@company.com",
        "position": "Accountant",
        "office": "105",
        "skype": "anna.brown"
    },
    "Michael Davis": {
        "phone": "808-333-4444",
        "email": "michael.davis@company.com",
        "position": "Developer",
        "office": "310",
        "skype": "michael.davis"
    },
    "Emily Wilson": {
        "phone": "808-444-5555",
        "email": "emily.wilson@company.com",
        "position": "HR Specialist",
        "office": "204",
        "skype": "emily.wilson"
    },
    "David Miller": {
        "phone": "808-555-6666",
        "email": "david.miller@company.com",
        "position": "Sales Manager",
        "office": "118",
        "skype": "david.miller"
    }
}

def find_worker(workers):
    print("\tPlease enter a name".center(90))
    worker = input("_" * 43 + ">").strip()
    found = workers.get(worker)
    if found is None:
        print("No such employee")
    else:
        for key, value in found.items():
            print(f"{key}: {value}")

def list_all_worker(workers):
    for numbers, name in enumerate(workers.keys(), start = 1):
        print(f"{numbers}. {name}")


def add_worker(workers):
    name = input("Please enter a name and last name: ").strip()
    phone = input("Please enter a phone number: ").strip()
    email = input("Please enter a email: ").strip()
    position = input("Please enter a position: ").strip()
    office = input("Please enter a office: ").strip()
    skype = input("Please enter a skype: ").strip()
    workers[name] = {
        "phone": phone,
        "email": email,
        "position": position,
        "office": office,
        "skype": skype
    }
    print(f"New employee {name} was added")

def change_worker_info(workers):
    print("\tPlease enter a name".center(90))
    worker = input("_" * 43 + ">").strip()
    found = workers.get(worker)
    if found is None:
        print("No such employee")
    else:
        print("1. Change phone".center(90))
        print("2. Change email".center(90))
        print("3. Change position".center(90))
        print("4. Change office".center(90))
        print("5. Change skype".center(90))
        print("Enter your chosen option below".center(90))
        for key, value in found.items():
            print(f"{key}: {value}")
        choice = input("_" * 43 + ">").strip()
        if choice == "1":
            workers[worker]["phone"] = input("Enter new phone number").strip()
        elif choice == "2":
            workers[worker]["email"] = input("Enter new email").strip()
        elif choice == "3":
            workers[worker]["position"] = input("Enter new position").strip()
        elif choice == "4":
            workers[worker]["office"] = input("Enter new office").strip()
        elif choice == "5":
            workers[worker]["skype"] = input("Enter new skype").strip()
        else:
            print("Wrong option")

def remove_employee(workers):
    print("Please enter a name".center(90))
    worker = input("_" * 43 + ">").strip()
    if worker in workers:
        print(f"WARNING".center(90))
        time.sleep(1)
        print(f"WARNING".center(90))
        time.sleep(1)
        print("To confirm enter 'yes' to cancel enter 'no'".center(90, "!"))
        choice = input("_" * 43 + ">").strip().lower()
        if choice == "yes":
            workers.pop(worker, None)
            print(f"Employee {worker} was removed")
        else:
            print(f"Employee {worker} was not removed")
    else:
        print("Employee not found")

def menu_print_company():
    print("Welcome to Company LLC directory.".center(90, "-"))
    print("Choose any option".center(90))
    print("To add an employee enter '1'".center(90))
    print("To remove an employee enter '2'".center(90))
    print("To find an employee enter '3'".center(90))
    print("To change an employee info enter '4'".center(90))
    print("To see the whole stuff directory '5'".center(90))
    print("To quit enter 'exit'".center(90))

def menu_input_company():
    menu_print_company()
    while True:
        choice = input("_" * 26 + " Choose option" +  "__>").lower().strip()
        if choice == "exit":
            break
        elif choice == "1":
            add_worker(company)
        elif choice == "2":
            remove_employee(company)
        elif choice == "3":
            find_worker(company)
        elif choice == "4":
            change_worker_info(company)
        elif choice == "5":
            list_all_worker(company)
        else:
            print("Wrong option")

# menu_input_company()

# Створіть програму «Книжкова колекція», яка зберігає інформацію про книги:
# автор, назва книги, жанр, рік випуску, кількість сторінок, видавництво.
# Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані.
# Використовуйте словник для збереження інформації.

books = {
    "Dune": {
        "author": "Frank Herbert",
        "genre": "Science Fiction",
        "year": 1965,
        "pages": 412,
        "publisher": "Chilton Books"
    },
    "The Hobbit": {
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": 1937,
        "pages": 310,
        "publisher": "George Allen & Unwin"
    },
    "1984": {
        "author": "George Orwell",
        "genre": "Dystopian Fiction",
        "year": 1949,
        "pages": 328,
        "publisher": "Secker & Warburg"
    },
    "The Old Man and the Sea": {
        "author": "Ernest Hemingway",
        "genre": "Literary Fiction",
        "year": 1952,
        "pages": 127,
        "publisher": "Charles Scribner's Sons"
    },
    "Harry Potter and the Sorcerer's Stone": {
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "year": 1997,
        "pages": 309,
        "publisher": "Bloomsbury"
    }
}

def find_book(libras):
    print("\tPlease enter a name".center(90))
    worker = input("_" * 43 + ">").strip()
    found = libras.get(worker)
    if found is None:
        print("No such book")
    else:
        for key, value in found.items():
            print(f"{key}: {value}")


def list_all_books(libras):
    for numbers, name in enumerate(libras.keys(), start=1):
        print(f"{numbers}. {name}")


def add_book(libras):
    title = input("Please enter title: ").strip()
    author = input("Please enter author name: ").strip()
    genre = input("Please enter genre: ").strip()
    year = int(input("Please enter a year: "))
    pages = int(input("Please enter number of pages: "))
    publisher = input("Please enter publisher: ").strip()
    libras[title] = {
        "author": author,
        "genre": genre,
        "year": year,
        "pages": pages,
        "publisher": publisher
    }
    print(f"New book '{title}' was added")


def change_book_info(libras):
    print("\tPlease enter a title".center(90))
    title = input("_" * 43 + ">").strip()
    found = libras.get(title)
    if found is None:
        print("No such book")
    else:
        print("1. Change author".center(90))
        print("2. Change genre".center(90))
        print("3. Change year".center(90))
        print("4. Change number of pages".center(90))
        print("5. Change publisher".center(90))
        print("Enter your chosen option below".center(90))
        for key, value in found.items():
            print(f"{key}: {value}")
        choice = input("_" * 43 + ">").strip()
        if choice == "1":
            libras[title]["author"] = input("Enter new author").strip()
        elif choice == "2":
            libras[title]["genre"] = input("Enter new genre").strip()
        elif choice == "3":
            libras[title]["year"] = int(input("Enter new year"))
        elif choice == "4":
            libras[title]["pages"] = int(input("Enter new number of pages"))
        elif choice == "5":
            libras[title]["publisher"] = input("Enter new publisher").strip()
        else:
            print("Wrong option")


def remove_book(libras):
    print("Please enter a title".center(90))
    book = input("_" * 43 + ">").strip()
    if book in libras:
        print(f"WARNING".center(90))
        time.sleep(1)
        print(f"WARNING".center(90))
        time.sleep(1)
        print("To confirm enter 'yes' to cancel enter 'no'".center(90, "!"))
        choice = input("_" * 43 + ">").strip().lower()
        if choice == "yes":
            libras.pop(book, None)
            print(f"Book {book} was removed")
        else:
            print(f"Book {book} was not removed")
    else:
        print("Book not found")


def menu_print_books():
    print("Welcome to Library directory.".center(90, "-"))
    print("Choose any option".center(90))
    print("To add a book enter '1'".center(90))
    print("To remove a book enter '2'".center(90))
    print("To find a book enter '3'".center(90))
    print("To change a book's info enter '4'".center(90))
    print("To see the whole library directory '5'".center(90))
    print("To quit enter 'exit'".center(90))


def menu_input_books():
    menu_print_books()
    while True:
        choice = input("_" * 26 + " Choose option" + "__>").lower().strip()
        if choice == "exit":
            break
        elif choice == "1":
            add_book(books)
        elif choice == "2":
            remove_book(books)
        elif choice == "3":
            find_book(books)
        elif choice == "4":
            change_book_info(books)
        elif choice == "5":
            list_all_books(books)
        else:
            print("Wrong option")

menu_input_books()


