for _ in range(10):
	n = int(input())
	ans = ""
	s = set()
	for f in range(1, n):
	    if n % f == 0:
	        s.add(f)
	for __ in range(5):
		x, y = map(int, input().split())
		c = 0
		x, y = x - 1, y - 1
		for f in s:
			if (x // f + y // f) % 2 == 0:
				c += 1
		ans += "G" if (c % 2) == 1 else "B"
	print(ans)