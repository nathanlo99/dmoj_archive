q = raw_input()
n = int(raw_input())
d = sorted(map(int, raw_input().split()))
j = sorted(map(int, raw_input().split()))
if q == '2': j = j[::-1]

c = 0
for a, b in zip(d, j):
	c += a if a > b else b
print(c)