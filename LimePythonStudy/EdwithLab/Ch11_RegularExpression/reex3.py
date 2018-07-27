import re

x = 'My favorite 2 number is 92 and 48!!'
y = re.findall('[0-9]+', x)
print(y)
