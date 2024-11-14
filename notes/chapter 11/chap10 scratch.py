(x, y) = (99, 'fred')
print(x)
print(y)
print(x, y)

d = {'a': 22, 'c': 34, 'b': 41, 'e': 62, 'd': 82}
print(d)
t = sorted(d.items())
print(t)

baliktad = list()
for k, v in d.items():
    baliktad.append((v, k))

print(baliktad)
sortat = sorted(baliktad, reverse=True)
print(sortat)
