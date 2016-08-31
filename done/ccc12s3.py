import sys
input = sys.stdin.readline

d = {}
for _ in xrange(int(input())):
	i = int(input())
	d[i] = d.get(i, 0) + 1

first = max(d.values())
first_vals = [x for x in d if d[x] == first]
for i in first_vals:
	d[i] = 0

if len(first_vals) >= 2:
	print(max(first_vals) - min(first_vals))
else:
	first = first_vals[0]
	second = max(d.values())
	print(max(abs(k - first) for k, v in d.items() if v == second))