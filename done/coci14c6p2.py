import sys
input = sys.stdin.readline

formations = []
for i in xrange(int(input())):
    o, v, n = map(int, input().split('-'))
    formations.append((o, v, n))

poss = set({(0, 0, 0)})
for _ in xrange(int(input())):
    new = set()
    s = input()
    if "O" in s:
        for o, v, n in poss:
            new.add((o + 1, v, n))
    if "V" in s:
        for o, v, n in poss:
            new.add((o, v + 1, n))
    if "N" in s:
        for o, v, n in poss:
            new.add((o, v, n + 1))
    poss.update(new)

for formation in formations:
    print("DA" if formation in poss else "NE")