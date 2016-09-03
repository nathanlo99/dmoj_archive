import sys

c = [int(x) for x in input()]
if 0 not in c or (sum(c) % 3 != 0): print(-1)
else: print("".join(map(str, sorted(c, reverse=True))))