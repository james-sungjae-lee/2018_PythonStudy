import re

hand = open('mbox_short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:')>=0:
        print(line)
