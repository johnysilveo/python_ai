import re
import time



text = ("Beautiful is better than ugly."
        "Explicit is better than implicit."
        "Explicit is better than implicit."
        "Simple is better than complex."
        "Complex is better than complicated."
        "Flat is better than nested."
        "Sparse is better than dense."
        "Readability counts."
        "Special cases aren't special enough to break the rules."
        "Although practicality beats purity."
        "Errors should never pass silently."
        )

def count_sentences(text):
    senteces = re.findall(r"[A-Z}[^.?!]*[.?!]",text)
    return len(senteces)

# print(f"{count_sentences(text):^90}")
# time.sleep(2)

def if_palindrome():
    print("=" * 90)
    print(f"{'Check if palindrome':^90}")
    print(f"{'Enter a word:':^90}")
    word = input("_" *43 + ">")
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", word).lower()
    reversed_word = cleaned[::-1]
    if cleaned == reversed_word:
        print(f"{f'{word} is palindrome':^90}")
        return True
    else:
        print(f"{f'{word} is not palindrome':^90}")
        return False


reserved_words = {"hello","goodbye","my","name","city"}
print("=" * 90)
print(f"{'Enter some text':^90}")
user_text = input("_" *43 + ">")
pattern = r"\b(hello|goodbye|my|name|city)\b"
cleaned_user_text = re.sub(pattern, lambda match: match.group().upper(),user_text)
print(f"{f'{cleaned_user_text}':^90}")

def find_and_delete():
    reserved_words = {"hello", "goodbye", "my", "name", "city"}
    print("=" * 90)
    print(f"{'Enter some text':^90}")
    user_text = input("_" * 43 + ">")
    print(f"{'Enter first symbol':^90}")
    char1 = input("_" * 43 + ">")
    print(f"{'Enter second symbol':^90}")
    char2 = input("_" * 43 + ">")
    pattern = r"\b(" + "|".join(reserved_words) + r")\b"
    start = user_text.find(char1)
    end = user_text.find(char2)
    if start == -1 or end == -1:
        return "One or both symbols were not found"
    if start > end:
        return "The first symbol comes after the second symbol"
    final_text = user_text[:start] + user_text[end + 1:]
    cleaned_final_text = re.sub(pattern, lambda match: match.group().upper(), final_text)
    return cleaned_final_text

# print("=" * 90)
# print(f"{find_and_delete():^90}")
# print("=" * 90)


def find_and_delete_on_ur_choice():
    print("=" * 90)
    print(f"{'Enter some text':^90}")
    user_text = input("_" * 43 + ">")
    print(f"{'Enter symbol(s)':^90}")
    user_chars = input("_" * 43 + ">")
    pattern = r"\b\w*[" + re.escape(user_chars) + r"]\w*\b"
    result = re.sub(pattern, "", user_text)
    result = re.sub(r"\s+", " ", result).strip()
    return result

print("=" * 90)
print(f"{find_and_delete_on_ur_choice():^90}")
print("=" * 90)

def reverse_text_by_words():
    print("=" * 90)
    print(f"{'Enter some text':^90}")
    user_text = input("_" * 43 + ">")

    words = user_text.split()
    reversed_words = words[::-1]
    final_text = " ".join(reversed_words)

    return final_text


print("=" * 90)
print(f"{reverse_text_by_words():^90}")
print("=" * 90)


