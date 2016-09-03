a = int(input())
b = int(input())

c = sum(1 for i in range(1, a + 1) if 10 - i in range(1, b + 1))

if c == 1:
	print("There is 1 way to get the sum 10.")
elif c <= 0:
	print("There are 0 ways to get the sum 10.")
else:
	print("There are", c, "ways to get the sum 10.")