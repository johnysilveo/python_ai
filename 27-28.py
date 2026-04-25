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

menu_input_word()