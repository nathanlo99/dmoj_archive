n = int(input())

for _ in range(n):
	k = int(input())
	c = sum(i for i in range(1, k) if k % i == 0)
	if c < k:
		print(k, "is a deficient number.")
	elif c == k:
		print(k, "is a perfect number.")
	else:
		print(k, "is an abundant number.")
