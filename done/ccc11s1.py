s, t = 0, 0
for _ in range(int(input())):
    for c in input():
        if c in ['s', 'S']:
            s += 1
        elif c in ['t', 'T']:
            t += 1
if s >= t:
    print("French")
else:
    print("English")
