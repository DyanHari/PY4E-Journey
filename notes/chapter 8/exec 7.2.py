# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")


total = 0
dividend = 0


try:
    fh = open(fname)

except:
    print('The file name you enter does not exist!')
    quit()

for line in fh:
    line = line.strip()

    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos1 = line.find(':')
    slice = line[pos1 + 1:len(line)]
    total = total + float(slice)
    dividend = dividend + 1

print('Average spam Confidence:', total / dividend)