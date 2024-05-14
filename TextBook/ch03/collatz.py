def collatz(n):
    return [n] + collatz(n // 2) if n % 2 == 0 else [n] + collatz(3 * n + 1) if n != 1 else [1]

def main():
    number = int(input("整数を入力してください: "))
    print(*collatz(number), sep="\n")

if __name__ == "__main__":
    main()

