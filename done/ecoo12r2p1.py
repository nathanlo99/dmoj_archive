def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)

d = " ABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?"

for _ in range(5):
	s = list(map(int, input().split()))[1:]
	p = s[0]
	for i in s[1:]:
		p = gcd(p, i)


	for pp in range(2, 500000):
		ans = ""
		if p % pp != 0:
			continue
		for i in s:
			ch = i // pp
			a, b = ch // 100, ch % 100
			if 0 <= a <= 30 and 0 <= b <= 30:
				ans += d[a] + d[b]
			else:
				break
		else:
			print(ans)
			break