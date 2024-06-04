from pathlib import Path
import re

def search(di, pattern):
    regex = re.compile(pattern)
    for file_path in Path(di).rglob('*.txt'):
        with file_path.open(encoding='utf-8') as file:
            for i, line in enumerate(file, 1):
                if regex.search(line):
                    print(f'ファイル: {file_path} - 行 {i}: {line.strip()}')

def main():
    di = input('ディレクトリを指定してください: ')
    pattern = input('検索する正規表現を入力してください: ')
    search(di, pattern)

if __name__ == '__main__':
    main()

