c = 0
for i in range(6):
	if input() == "W":
		c += 1
print([-1, 3, 3, 2, 2, 1, 1][c])
# print([-1, 3, 3, 2, 2, 1, 1][sum(1 for x in range(6) if input() == "W")])