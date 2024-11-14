import re
fhand = open('../../chapter 12/mbox-short.txt')

numlist = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    print(stuff)