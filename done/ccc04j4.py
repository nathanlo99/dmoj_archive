key = input()

for (n, i) in enumerate(c for c in input() if ord(c) in range(ord('A'), ord('Z') + 1)):
	print(chr(ord('A') + (ord(i) + ord(key[n % len(key)])) % 26), end="")
