a = input()
b = input()
d = {}
for c in a:
    d[c] = d.get(c, 0) + 1
for c in b:
    d[c] = d.get(c, 0) - 1
sum = 0
for v in d.values():
    sum += abs(v)
print(sum)
