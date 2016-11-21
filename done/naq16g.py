import math
import sys
input = sys.stdin.readline

n = input().strip()
f = ["1", "2", "6", "24", "120"]
if n in f:
    print(f.index(n) + 1)
else:
    a = 0
    b = len(n)
    i = 1
    while a < b:
        a += math.log10(i)
        if a < b:
            i += 1
        else:
            break
    print(i - 1)