import re
fhand = open('../../chapter 12/regex_sum_2110048.txt')

numlist = list()
for line in fhand:
    stuffs = re.findall('([0-9]+)', line)
    if len(stuffs) < 1: continue
    print(stuffs)
    for num in stuffs:
        numbers = int(num)
        numlist.append(numbers)

print(numlist)
print(len(numlist))
print(sum(numlist))