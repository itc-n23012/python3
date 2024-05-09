import random
secret_number = random.randint(1,20)
print('1から20までの数を当ててください。')

for i in range(6):
    print("数を入力してください。")
    guess = int(input())
    if guess < secret_number:
        print('あなたの推定値は小さいです')
    elif guess > secret_number:
        print('あなたの推定値は大きいです')
    else:
        break

if guess == secret_number:
    print('当たり！' + str(i +1) +'回であたりました')
else:
    print('残念。正解は'+str(secret_number) + 'でした')