import sys
k = sys.stdin.read().split("\n")[1:-1]
d = []
for x in k:
     if x == "0": d.pop()
     else: d.append(int(x))
print(sum(d))
