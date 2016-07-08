amts = [0, 100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
total = 1691600
cases = 10
for _ in range(int(input())):
	total -= amts[int(input())]
	cases -= 1
if int(input()) * cases > total: print("deal")
else: print("no deal")
