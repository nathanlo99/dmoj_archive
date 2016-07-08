for _ in range(int(input())):
	b = bin(int(input()))[2:]
	b = "0" * ((-len(b)) % 4) + b
	print(" ".join(b[i:i + 4] for i in range(0, len(b), 4)))
