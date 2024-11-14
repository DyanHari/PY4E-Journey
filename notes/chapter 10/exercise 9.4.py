name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
    if not line.startswith('From:'):
        continue
    words = line.split()
    emails = [words[1]]
    for email in emails:
        count[email] = count.get(email, 0) + 1

bigword = None
bigcount = None

for email,count in count.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count

print(bigword, bigcount)






