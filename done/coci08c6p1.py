a = len(input()) - 1
op = input()
b = len(input()) - 1

if op == "*":
	line = "1" + "0" * (a + b)
	print(line)
elif a != b:
	m = max(a, b)
	n = a + b - m
	line = "1" + "0" * (m - n - 1) + "1" + "0" * n
	print(line)
else:
    line = "2" + "0" * a
    print(line)