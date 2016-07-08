d = input()
while(d != 'quit!'):
	if len(d) > 4 and d[-3] not in ['a', 'e', 'i', 'o', 'u'] and d[-2:] == "or":
		d = d[:-1] + "u" + d[-1]
	print(d)
	d = input()
