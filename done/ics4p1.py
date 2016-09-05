import sys
input = sys.stdin.readline

s = input()
t = []

def solve(n, s="", used=[]):
	for i in n:
		if i not in used:
			solve(n, s + i, used + [i])
	if len(s) == len(n):
		global t
		t.append(s)

solve(s)
for i in sorted(t):
	print(i)