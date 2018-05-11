x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

print(min((x1-x2)**2+(y1-y2)**2,(x2-x3)**2+(y2-y3)**2,(x3-x1)**2+(y3-y1)**2))