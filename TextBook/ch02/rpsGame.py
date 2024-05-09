import random

def main():
    user_win_count = 0
    computer_win_count = 0
    draw_count = 0

    while True:
        user = int(input("じゃんけんをします（0: グー, 1: パー, 2: チョキ、または終わりのいずれかを選んでください）："))
        
        if user == '終わり':
            print("ゲームを終了します。")
            break

        computer = random.randint(0, 2)

        print(f"あなた: {user}")
        print(f"コンピュータ: {computer}")

        result = (user - computer) % 3
        if result == 0:
            print("引き分けです！")
            draw_count += 1
        elif result == 1:
            print("あなたの勝ちです！")
            user_win_count += 1
        else:
            print("コンピュータの勝ちです！")
            computer_win_count += 1

        print(f"現在の勝ち数：あなた {user_win_count}勝, コンピュータ {computer_win_count}勝, 引き分け {draw_count}回\n")

main()
