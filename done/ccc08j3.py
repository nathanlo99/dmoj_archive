keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ -.*"
string = input() + "*"
steps = 0
current = 'A'
for i in string:
    i1 = keys.index(current)
    i2 = keys.index(i)
    steps += abs(i1 % 6 - i2 % 6) + abs(i1 // 6 - i2 // 6)
    current = i
print(steps)
