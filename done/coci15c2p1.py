from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
b = "22233344455566677778889999"
l = "abcdefghijklmnopqrstuvwxyz"
k = {letter: button for letter, button in zip(l, b)}

d = defaultdict(int)
for i in range(n):
    s = input().strip()
    num = 0
    for c in s:
        num = 10 * num + int(k[c])
    d[num] += 1
k = int(input())
print(d[k])