import sys, pyperclip

TEXT = {'agree': 'そうですね',
             'busy': 'すみません',
             'upsell': 'これを毎日'}

if len(sys.argv) < 2:
    sys.exit(' python mclip.py [キーフレーズ名] \n キーフレーズに対応するテキストをクリップボードにコピーします')

keyphrase = sys.argv[1]

pyperclip.copy(TEXT[keypkrase]),print(keyphrase + 'のキーフレーズをクリップボードにコピーしました') if keyphrase in  TEXT else print(ketphrase + 'に対応するテキストがありません')

