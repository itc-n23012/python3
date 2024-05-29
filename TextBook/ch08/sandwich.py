import pyinputplus as p

PRICE = {
    'チーズ': 50,
    'ハム': 100,
    'ターキー': 120,
    '鶏肉': 110,
    '小麦パン': 30,
    'ライ麦パン': 35,
    '白パン': 25,
    'yes': 10,
    'no': 0
}

def make_sandwich():
    sandwich_type = p.inputMenu(['チキン', 'ハム', 'ターキー', '豆腐'], numbered=True)
    bread_type = p.inputMenu(['小麦パン', 'サワー種', '白パン'], numbered=True)
    mayonnaise = p.inputYesNo('マヨネーズを追加しますか？ (yes/no): ')
    mustard = p.inputYesNo('マスタードを追加しますか？ (yes/no): ')
    lettuce = p.inputYesNo('レタスを追加しますか？ (yes/no): ')
    tomato = p.inputYesNo('トマトを追加しますか？ (yes/no): ')
    cheese = p.inputYesNo('チーズを追加しますか？ (yes/no): ')
    quantity = p.inputInt('何個のサンドイッチを作りますか？ ', min=1)

    # 合計金額を計算する
    total = (PRICE[sandwich_type] + PRICE[bread_type] +
                   PRICE[mayonnaise] + PRICE[mustard] +
                   PRICE[lettuce] + PRICE[tomato] + PRICE[cheese]) * quantity

    print('\n注文内容:')
    print(f'サンドイッチの種類: {sandwich_type}')
    print(f'パンの種類: {bread_type}')
    print(f'マヨネーズ: {"追加" if mayonnaise == "yes" else "追加しない"}')
    print(f'マスタード: {"追加" if mustard == "yes" else "追加しない"}')
    print(f'レタス: {"追加" if lettuce == "yes" else "追加しない"}')
    print(f'トマト: {"追加" if tomato == "yes" else "追加しない"}')
    print(f'チーズ: {"追加" if cheese == "yes" else "追加しない"}')
    print(f'数量: {quantity}')
    print(f'合計金額: {total_price} 円')

make_sandwich()

