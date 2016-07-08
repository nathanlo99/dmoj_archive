n = int(input())
s = (n * (n + 1)) // 2
for i in range(n - 1):
	s -= int(input())
print(s)
