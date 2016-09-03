for _ in range(10):
	n = int(input())
	spinner = set(map(int, input().split()))
	targets = map(int, input().split())
	poss = set(spinner)
	temp = set(poss)
	for i in temp:
		for j in spinner:
			poss.add(i + j)
			poss.add(i * j)
	temp = set(poss)
	for i in temp:
		for j in spinner:
			poss.add(i + j)
			poss.add(i * j)
	for target in targets:
		print("T" if target in poss else "F", end="")
	print()