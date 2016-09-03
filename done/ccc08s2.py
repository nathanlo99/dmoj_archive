x = int(input())
while x != 0:
	print(sum(2 * int(((x * x - i * i) ** 0.5)) + 1 for i in range(-x, x + 1)))
	x = int(input())