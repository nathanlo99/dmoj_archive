import sys
input = sys.stdin.readline

input()
s = sorted(map(int, input().split()))
a = min(s[i + 1] - s[i] for i in range(0, len(s) - 1))
print(a)