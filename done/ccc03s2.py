def rhymes(a, b):
	a_last = -1
	b_last = -1
	for c in ['a', 'e', 'i', 'o', 'u']:
		if a.rfind(c) > a_last:
			a_last = a.rfind(c)
		if b.rfind(c) > b_last:
			b_last = b.rfind(c)
	a_end = a[a_last:] if a_last != -1 else a
	b_end = b[b_last:] if b_last != -1 else b
	return a_end == b_end

for _ in range(int(input())):
	a = []
	for __ in range(4): 
		a.append(input().split()[-1].lower())
	if rhymes(a[0], a[1]) and rhymes(a[2], a[3]):
		if rhymes(a[0], a[2]):
			print("perfect")
		else:
			print("even")
	elif rhymes(a[0], a[2]) and rhymes(a[1], a[3]):
		print("cross")
	elif rhymes(a[0], a[3]) and rhymes(a[1], a[2]):
		print("shell")
	else:
		print("free")