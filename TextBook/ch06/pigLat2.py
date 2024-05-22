def pig_latin(text):
    words = []
    for word in text.split():
        if word.isalpha():
            if word[0].lower() in 'aeiou':
                words.append(word + 'yay')
            elif word[:2].lower() not in 'aiueo':
                words.append(word[2:] + word[:2] + 'ay')
            else:
                words.append(word[1:] + word[0] + 'ay')
        else:
            words.append(word)
    return ' '.join(words)

text = input()
print(pig_latin(text))

