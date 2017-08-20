import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
words = defaultdict(int)
for i in range(n):
    words[input().strip()] += 1
print(sum(1 for v in words.values() if v == 1))