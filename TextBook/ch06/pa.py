def pig_latin(text):
    return ' '.join((word + 'yay') if word[0].isalpha() and word[0] in 'aeiouAEIOU' else (word[2:] + word[:2] + 'ay') if word[:1].isalpha() and word[:2] not in 'gaeiouAEIOU' else (word[1:] + word[0] + 'ay') if word[0].isalpha() else (word[2:] + word[:2] + 'ay') if word[:1].isalpha() and word[:2] not in 'gaeiouAEIOU'else word for word in text.split())

text = input()
print(pig_latin(text))

