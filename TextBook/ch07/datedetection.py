import re

day = r'(0[1-9]|[12][0-9]|3[01])'
mon = r'(0[1-9]|1[0-2])'
year = r'(1000|1[1-9][0-9]{2}|2[0-9]{3})'

date = f'{day}/{mon}/{year}'

date_regex = re.compile(date)

dmy = input('日付/月/年: ')

print('True' if date_regex.fullmatch(dmy) else 'False')

