n, p = map(int, input().split())
names = []
times = [0] * n
for i in range(n):
	names.append(input().strip())
for i in range(p):
	s = list(map(int, input().split()))
	for j in range(n):
		times[j] += s[j]
r = 3
for rank in sorted(zip(names, times), key = lambda x: x[1], reverse=True):
	print(str(r) + '.', rank[0])
	r += 1