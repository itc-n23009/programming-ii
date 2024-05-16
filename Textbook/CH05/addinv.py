def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1

def display_inventory(inventory):
    print("持ち物リスト:")
    total_items = sum(inventory.values())
    for item, count in inventory.items():
        print(f"    {count} {item}")
    print(f"アイテム総数: {total_items}")

inv = {'金貨': 42, 'ロープ': 1}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
