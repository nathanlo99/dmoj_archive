from math import sqrt, floor

n = int(input())

for i in range(floor(sqrt(n)) + 1, 1, -1):
	if n % i == 0:
		t = int(n / i)
		print(i + i + t + t)
		break
else:
    pass
