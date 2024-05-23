import re
from datetime import datetime

date_regex = re.compile(r"""
    (0[1-9]|[12][0-9]|3[01])
    /
    (0[1-9]|1[0-2])
    /
    ([12]\d{3})
    """, re.VERBOSE)

def is_valid_date(day, month, year):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

user_input = input()

match = date_regex.fullmatch(user_input)
if match:
    day, month, year = map(int, match.groups())
    if is_valid_date(day, month, year):
        print(f"{user_input} は有効な日付です。")
    else:
        print(f"{user_input} は無効な日付です。")
else:
    print(f"{user_input} は正しい形式ではありません。")
