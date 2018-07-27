import re

hand = open('mbox_short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\S*:', line):
        print(line)
