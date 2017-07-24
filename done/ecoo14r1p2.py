def convert(a, idx):
	try:
		ans = 0
		for i in range(idx, idx + 8):
			ans = 2 * ans + a[i]
		return ans
	except IndexError:
		return None

def ans(a, b):
	for offset in range(0, 8):
		res = ""
		for start in range(offset, 10000, 8):
			t = convert(a, start)
			if t is None:
				return res
			if not (t == 32 or 65 <= t <= 90):
				break
			else:
				res += chr(t)

		res = ""
		for start in range(offset, 10000, 8):
			t = convert(b, start)
			if t is None:
				return res
			if not (t == 32 or 65 <= t <= 90):
				break
			else:
				res += chr(t)

for _ in range(10):
	_, s = input(), input()
	a, b = [], []
	for c in s:
		a.append(0 if c in "AT" else 1)
		b.append(1 if c in "AT" else 0)
	print(ans(a, b))