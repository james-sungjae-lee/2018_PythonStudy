import re

hand = open('mbox_short.txt')
numlist = []
for line in hand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) is not 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print(max(numlist))
