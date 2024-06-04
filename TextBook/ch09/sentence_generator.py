import re

with open('input.txt', 'r') as file:
    text = file.read()

for keyword in re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB', text):
    rep = input(f'{keyword.lower()}を入力してください: ')
    text = text.replace(keyword, rep, 1)

print('\n結果:\n', text)
with open('output.txt', 'w') as file:
    file.write(text)

