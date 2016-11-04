import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())

t = []
for i in xrange(len(s) - n + 1):
	t.append(s[i:i+n])
print(min(t))