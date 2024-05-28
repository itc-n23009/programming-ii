import pyinputplus as pyip

item_prices = {
    '小麦パン': 100,
    '白パン': 80,
    'サワー種': 120,
    'チキン': 200,
    'ターキー': 180,
    'ハム': 150,
    '豆腐': 100,
    'チーズ': {'チェダー': 50, 'スイス': 60, 'モッツアレラ': 70},
    'マヨネーズ': 30,
    'からし': 20,
    'レタス': 15,
    'トマト': 25,
    'なし': 0,
}

def get_menu_choice(prompt, choices):
    return pyip.inputMenu(choices, prompt=prompt, numbered=True)

def get_yes_no(prompt):
    return pyip.inputYesNo(prompt)

def calculate_total(items):
    total = sum(item_prices[item] if isinstance(item_prices[item], int) else sum(item_prices[item].values()) for item in items)
    return total

bread_choices = ['小麦パン', '白パン', 'サワー種']
bread = get_menu_choice('パンの種類を選んでください:\n', bread_choices)

protein_choices = ['チキン', 'ターキー', 'ハム', '豆腐']
protein = get_menu_choice('タンパク質の種類を選んでください:\n', protein_choices)

cheese_needed = get_yes_no('チーズは必要ですか？\n')

if cheese_needed == 'yes':
    cheese_choices = ['チェダー', 'スイス', 'モッツアレラ']
    cheese = get_menu_choice('チーズの種類を選んでください:\n', cheese_choices)
else:
    cheese = 'なし'

toppings_needed = {
    'マヨネーズ': get_yes_no('マヨネーズは必要ですか？\n'),
    'からし': get_yes_no('からしは必要ですか？\n'),
    'レタス': get_yes_no('レタスは必要ですか？\n'),
    'トマト': get_yes_no('トマトは必要ですか？\n')
}

num_sandwiches = pyip.inputInt(prompt='サンドイッチがいくつ欲しいですか？: ', min=1)

items = [bread, protein]
if cheese_needed == 'yes':
    items.append('チーズ')
items.extend([topping for topping, needed in toppings_needed.items() if needed == 'yes'])

total_price = calculate_total(items)

print("\n選択した内容:")
print(f"パンの種類: {bread}")
print(f"タンパク質の種類: {protein}")
print(f"チーズ: {'必要' if cheese_needed == 'yes' else '不要'}")
if cheese_needed == 'yes':
    print(f"チーズの種類: {cheese}")
for topping, needed in toppings_needed.items():
    print(f"{topping}: {'必要' if needed == 'yes' else '不要'}")
print(f"サンドイッチの数: {num_sandwiches}")
print(f"合計金額: {total_price} 円")


