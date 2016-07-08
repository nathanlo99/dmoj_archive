c = int(input())
r, w, b, y, g = map(int, input().split())

print(max(0, c - (r - 1)//4 - (w - 1)//5- (b - 1)//4 - (y - 1)//3 - (g - 1)//6 - 5))
