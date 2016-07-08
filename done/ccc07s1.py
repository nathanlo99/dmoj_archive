for _ in range(int(input())):
	y, m, d = map(int, input().split())
	print ("Yes" if y * 10000 + m * 100 + d <= 19890227 else "No")
