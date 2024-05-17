def display_inventory(inventory):
    print("持ち物リスト:")
    for k, v in inventory.items():
        print(f"{v} {k}")
    print(f"アイテム総数: {sum(inventory.values())}")
if __name__ == "__main__":
    a = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}
    display_inventory(a)
