def pig_latin(text):
    return ' '.join((word + 'yay') if word[0].isalpha() and word[0] in 'aeiouAEIOU' else word[2:] + word[:2] + 'ay' if word[0] not in 'aiueoAIUEO' and word[1] not in 'aiueoAIUEO' and word[:2].isalpha() else (word[1:] + word[0] + 'ay') if word[0].isalpha() else word for word in text.split())

text =input() 
print(pig_latin(text))

