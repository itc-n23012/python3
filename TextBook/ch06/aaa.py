def print_table(text):
    # 各列の最大の文字数を見つける
    max_lengths = [max(len(item) for item in column) for column in text]

    # 転置された表を生成
    transposed = []
    for row in zip(*text):
        transposed_row = []
        for i in range(len(row)):
            transposed_row.append(row[i].rjust(max_lengths[i]))
        transposed.append(transposed_row)

    # 転置された表を文字列に変換
    return '\n'.join(' '.join(row) for row in transposed)

text = [['apple', 'orange', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dog', 'cats', 'moose', 'goose']]

print(print_table(text))

