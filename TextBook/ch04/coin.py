from random import choice

count = sum(
    all(choice(['表', '裏']) == choice(['表', '裏']) for _ in range(6))
    for _ in range(10000)
)

kakuritu = count /10000 
print(f'6連続で同じ面が出る割合: {kakuritu* 100}%')

