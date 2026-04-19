import re





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

# print("=" * 90)
# print(f"{find_and_delete_on_ur_choice():^90}")
# print("=" * 90)


pattern = r"^[A-Za-z_][A-Za-z_0-9]{0,19}$"
print("Enter ur text to validate".center(90))
user_text = input("_" * 43 + ">")
if re.fullmatch(pattern, user_text):
    print("OK".center(90))
else:
    print("NO".center(90))