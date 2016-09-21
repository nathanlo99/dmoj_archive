import sys
input = sys.stdin.readline

n = int(input())
s = (n * (n + 1)) // 2
for i in xrange(n - 1):
	s -= int(input())
print(s)