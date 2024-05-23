import re

def is_strong_password(password):
    uppercase_regex = re.compile(r"[A-Z]")
    lowercase_regex = re.compile(r"[a-z]")
    digit_regex = re.compile(r"\d")

    if len(password) >= 8 and uppercase_regex.search(password) and lowercase_regex.search(password) and digit_regex.search(password):
        return True
    else:
        return False

def main():
    password = input("パスワードを入力してください: ")

    if is_strong_password(password):
        print("パスワードは強いです。")
    else:
        print("パスワードが弱いです。")

if __name__ == "__main__":
    main()


