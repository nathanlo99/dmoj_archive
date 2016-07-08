input()

a = 0
b = 0

for c in input():
	if c == "A": a += 1
	else: b += 1
print("A" if a > b else "B" if a < b else "Tie")
