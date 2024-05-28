import pyperclip, re

text = str(pyperclip.paste())
phone = re.compile(r'0[789][08]-[0-9]{3,4}-[0-9]{4}')
mail = re.compile(r'[a-zA-Z0-9._+\-%]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')

li = []

for num in phone.findall(text):
    li.append(num)

for add in mail.findall(text):
    li.append(add)


if len(li) > 0 :
    s = '\n'.join(li)
    pyperclip.copy(s)
    print(s)
else:
    print('ありませんでした')


