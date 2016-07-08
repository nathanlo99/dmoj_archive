for _ in range(5):
	for num in map(lambda x: x[::-1], input().split()):
		print((10 - (sum([0, 2, 4, 6, 8, 1, 3, 5, 7, 9][int(c)] for c in num[::2]) + sum(int(c) for c in num[1::2]))) % 10, end="")
	print()
