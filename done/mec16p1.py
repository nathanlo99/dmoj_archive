from math import atan2, degrees

r, c = map(int, input().split())
wounds = []
for i in range(r):
    s = input()
    for j, c in enumerate(s):
        if c == "X":
            wounds.append((j, i))
wounds.sort()
for i, (x, y) in enumerate(wounds):
    if i + 1 == len(wounds):
        break
    nx, ny = wounds[i + 1]
    print("{:.3f}".format(180 - degrees(atan2(nx - x, ny - y))))
else:
    print("0.000")
