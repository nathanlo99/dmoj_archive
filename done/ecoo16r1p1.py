for i in range(10):
	w = list(map(int, input().split()))
	c = 0
	for j in range(int(input())):
		x = list(map(int, input().split()))
		if sum(x[i] * w[i] for i in range(4)) >= 5000: c += 1
	print(c)