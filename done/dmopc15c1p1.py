MX = 0.0
MXNAME = ""

for _ in range(int(input())):
	name, val = input().split()
	if float(val) > MX: MXNAME = name; MX = float(val)

print(MXNAME)
