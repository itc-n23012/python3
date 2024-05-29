import pyinputplus as p, random, time

ok = 0
def ab():
    global ok
    for _ in range(10):
        num1, num2 = random.randint(0, 9), random.randint(0, 9)
        start = time.time()
        for _ in range(3):
            try:
                ans = p.inputInt(f'{num1} × {num2} = ')
                end = time.time()
                if ans == num1 * num2:
                    if end - start > 8:
                        print('時間切れ')
                    else:
                        print('正解')
                        ok += 1
                    break
                print('不正解')
            except p.RetryLimitException:
                print('回数制限')
ab()
print(f'正解数: {ok}')


