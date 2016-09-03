p = ['A', 'B', 'C', 'D', 'E']

while(True):
	button = input()
	number = int(input())
	if button == '4': break
	for _ in range(number):
		if button == '1': p = p[1:] + [p[0]]
		elif button == '2': p = [p[-1]] + p[:-1]
		elif button == '3': p = [p[1]] + [p[0]] + p[2:]
print(" ".join(p))