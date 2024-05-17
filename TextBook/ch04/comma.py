def comma(spam):
    return ','.join(spam[:-1]) + ', and' + spam[-1] + '.'
spam = ['apple', 'banana', 'tofu', 'cats']
print(comma(spam))
