import re

passwd = r'((?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,})' 
passwdd = input()

print('強い' if re.compile(passwd).fullmatch(passwdd) else '弱い')

