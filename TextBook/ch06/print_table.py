def print_table(text):
    max_len = [max(len(a) for a in i) for i in text]
    li = []
    for a in zip(*text):
        li_a = []
        for i in range(len(a)):
            li_a.append(a[i].rjust(max_len[i]))  
        li.append(li_a)
    return '\n'.join(' '.join(row) for row in li)  

text = [['apple', 'orange', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dog', 'cats', 'moose', 'goose']]

print(print_table(text))

