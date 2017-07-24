_, s = input(), input()

a = lambda n: "ABC"[n % 3]
b = lambda n: "BABC"[n % 4]
c = lambda n: "CAB"[(n // 2) % 3]

aa, bb, cc = 0, 0, 0
for i, char in enumerate(s):
	if char == a(i):
		aa += 1
	if char == b(i):
		bb += 1
	if char == c(i):
		cc += 1

dd = max(aa, bb, cc)
print(dd)

if aa == dd:
	print("Adrian")
if bb == dd:
	print("Bruno")
if cc == dd:
	print("Goran")