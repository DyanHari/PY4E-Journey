#startswith
line = 'Please have a nice day'
weh = line.startswith('please')
print(weh)

data = 'From johnharryduavis@gmail.com wed 23 october 2024 philippines'
pos1 = data.find('@')
print(pos1)

pos2 = data.find(' ', pos1)
print(pos2)

host = data[pos1 + 1 : pos2]
print(host)