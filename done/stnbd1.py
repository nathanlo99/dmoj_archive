n = int(input())
r = int(input())
for _ in range(n - 1):
	if int(input()) >= r:
		print("NO")
		break
else: print("YES")