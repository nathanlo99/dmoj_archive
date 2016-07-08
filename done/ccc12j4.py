k = int(input())

for (n, c) in enumerate(input()):
	print(chr(ord('A') + (ord(c) - ord('A') - 3 * n - k - 3) % 26),  end="")
