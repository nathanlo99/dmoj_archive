good = lambda n: all(i in "ABCEGLOR" for i in n)

def shift(i, s):
	res = ""
	for n, j in enumerate(i):
		res += chr((ord(j) - ord('A') + s[n]) % 26 + ord('A'))
	return res

def solve(i, s):
	for j in range(26):
		if not good(i): i = shift(i, s)
		else: return j
	return -1

for _ in range(int(input())):
	s = input().split()
	n = int(s[0])
	i = s[1]
	s = list(map(int, s[2:]))
	print(solve(i, s))