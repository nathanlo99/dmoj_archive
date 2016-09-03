m = {}
for _ in range(int(input())):
	a, b = input().split()
	m[b] = a
n = input()
while(n):
	for word in m:
		if n.startswith(word):
			n = n[len(word) :]
			print(m[word], end="")