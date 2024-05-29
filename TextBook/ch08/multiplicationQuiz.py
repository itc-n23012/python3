import pyinputplus as p, random

ok = 0
def ab():
    global ok
    for _ in range(10):
        num1, num2 = random.randint(0, 9), random.randint(0, 9)
        for _ in range(3):
            try:
                ans = p.inputInt(f'{num1} × {num2} = ', timeout=8)
                if ans == num1 * num2:
                    print('正解')
                    ok += 1
                    break
                print('不正解')
            except p.TimeoutException:
                print('時間切れ')
            except p.RetryLimitException:
                print('回数制限超え')

ab()
print(f'正解数: {ok}')

