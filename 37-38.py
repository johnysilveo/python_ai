def shout(text):                # Функція приймає text.
    return text.upper()         # Робить текст великими літерами.
def whisper(text):              # Інша функція приймає text.
    return text.lower()         # Робить текст маленькими літерами.
def speak(func, text):          # speak приймає іншу функцію як аргумент.
    return func(text)           # Запускає отриману функцію.
print(speak(shout, "Python")) # Передаємо shout без дужок.
print(speak(whisper, "Python")) # Передаємо whisper без дужок.


def my_decorator(func):                 # Decorator приймає оригінальну функцію.
    def wrapper():                      # Wrapper буде новою функцією.
        print("Before function")        # Код ДО запуску оригінальної функції.
        func()                          # Запускаємо оригінальну функцію.
        print("After function")             # Код ПІСЛЯ запуску оригінальної функції.
    return wrapper                      # Повертаємо wrapper, не викликаємо його.
def say_hi():                           # Оригінальна функція.
    print("Hi")                         # Основна логіка функції.
say_hi = my_decorator(say_hi)           # Ручне обгортання функції.
say_hi()                                # Насправді запускається wrapper.