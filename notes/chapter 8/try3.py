trying = open('harry.txt')

for line in trying:
    line = line.rstrip()
    if line.startswith('a'):
        print(line)
