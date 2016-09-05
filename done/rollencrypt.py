import sys
input = sys.stdin.readline
from collections import defaultdict

k = int(input())
count = defaultdict(int)
s = input().strip()
first = {}
for i, c in enumerate(s):
    if i >= k:
        m = max(count.items(), key=lambda x: (x[1], -ord(x[0])))
        shift = ord(m[0]) - ord("a") + 1
        print(chr(ord("a") + (ord(c) - ord("a") + shift + 26) % 26), end="")
        count[c] += 1
        count[s[i - k]] -= 1
    else:
        print(c, end="")
        count[c] += 1
print()