import re

def strip(text, rm):
    p = f'^{re.escape(rm)}+|{re.escape(rm)}+$'
    return re.sub(p, '', text)

text = input('テキストを入力してください: ')
rm = input('削除したい両端の文字を入力してください: ')

print(strip(text, rm))

