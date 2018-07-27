import re

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
z = re.findall('^F.+?:', x)

print(y)
print(z)
