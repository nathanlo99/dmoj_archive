combinations = []
min_tickets = None

def solve(a, b, c, d, n, cur=[0, 0, 0, 0]):
	if n >= a:
		solve(a, b, c, d, n - a, [cur[0] + 1, cur[1], cur[2], cur[3]])
	if n >= b:
		solve(a, b, c, d, n - b, [cur[0], cur[1] + 1, cur[2], cur[3]])
	if n >= c:
		solve(a, b, c, d, n - c, [cur[0], cur[1], cur[2] + 1, cur[3]])
	if n >= d:
		solve(a, b, c, d, n - d, [cur[0], cur[1], cur[2], cur[3] + 1])
	if n == 0:
		global min_tickets, combinations
		if min_tickets == None or sum(cur) < min_tickets:
			min_tickets = sum(cur)
		if cur not in combinations:
			print("# of PINK is " + str(cur[0]), end=" ")
			print("# of GREEN is " + str(cur[1]), end=" ")
			print("# of RED is " + str(cur[2]), end=" ")
			print("# of ORANGE is " + str(cur[3]), end=" ")
			print()
			combinations.append(cur)

solve(int(input()), int(input()), int(input()), int(input()), int(input()))
print("Total combinations is " + str(len(combinations)) + ".")
print("Minimum number of tickets to print is " + str(min_tickets) + ".")