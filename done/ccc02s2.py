def gcf(a, b):
	while a != b:
		if a > b: a -= b
		else: b -= a
	return a

def frac(a, b):
	g = gcf(a, b)
	return str(a // g) + "/" + str(b // g)

a = int(input())
b = int(input())

if a % b == 0: print(a // b)
elif a < b: print(frac(a, b))
else: print(a // b, frac(a % b, b))
