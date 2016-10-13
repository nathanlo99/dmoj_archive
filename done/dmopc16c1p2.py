import sys
from collections import defaultdict
input = sys.stdin.readline

lines = defaultdict(set)
ans = 0
for i in xrange(int(input())):
    m, b = map(int, input().split())
    if b in lines[m]:
        print("Infinity")
        sys.exit(0)
    ans += i - len(lines[m])
    lines[m].add(b)
print(ans)