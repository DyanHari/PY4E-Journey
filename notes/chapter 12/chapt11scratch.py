import re

fhand = open('../../chapter 12/mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
        finish = line

#greedy
x = 'From: Using the: characters'
y = re.findall('^F.+:', x)
print(y)

#non greedy
a = 'From: Using the: characters'
b = re.findall('^F.+?:', x)
print(b)

#at least one character na walang space sa magkabilang dulo
c = re.findall('\S+@\S+', finish)
print(c)