m = []
for _ in range(4):
	m.append(list(map(int, input().split())))
s = sum(m[0])
f = False
for i in range(1, 4):
	if sum(m[1]) != s:
		break
else:
	for i in range(4):
		if sum(m[j][i] for j in range(4)) != s:
			break
	else:
		print("magic")
		f = True
if not f:	print("not magic")
