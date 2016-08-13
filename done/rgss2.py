n = int(input())
minx, miny = map(int, input().split())
maxx, maxy = minx, miny
for i in range(n - 1):
	x, y = map(int, input().split())
	minx = min(minx, x)
	maxx = max(maxx, x)
	miny = min(miny, y)
	maxy = max(maxy, y)
print((maxx - minx) * (maxy - miny))
