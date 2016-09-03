a = int(input()) + 1
while True:
	if len(set(list(str(a)))) == len(str(a)): break
	else: a += 1
print(a)