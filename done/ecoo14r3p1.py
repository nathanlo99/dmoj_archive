s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,?"

def encode(c):
	return s.index(c) + 1

def decode(n):
	return s[n - 1]

for _ in range(10):
	sample_in = input().strip()[1:-1]
	sample_out = input().strip()[1:-1]
	for i in range(2, 67):
		for a, b in zip(sample_in, sample_out):
			aa, bb = encode(a), encode(b)
			if (bb * i) % 67 != aa:
				break
		else:
			d = i
			break
	text = input().strip()[1:-1]
	line = "*"
	for c in text:
		line += decode((encode(c) * d) % 67)
	print(line + "*")