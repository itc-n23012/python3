import random

guess = ''
while guess not in ('表', '裏'):
    guess = input('裏表を当ててください ')

toss = random.choice(['表', '裏'])

if toss == guess:
    print('当たり！')
else:
    guess = input('はずれ。もう一回表裏選んでください')
    print('当たり！' if toss == guess else 'アホか２択を連続で外すなよ')

