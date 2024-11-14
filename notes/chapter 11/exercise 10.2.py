name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
    if not line.startswith('From '):
        continue

    words = line.split()
    time = words[5]
    hours = time.split(':')
    sephours = [hours[0]]
    for hour in sephours:
        count[hour] = count.get(hour, 0) + 1

for k, v in sorted(count.items()):
    print(k, v)