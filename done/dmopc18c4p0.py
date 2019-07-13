r, x, y = map(int, input().split())
mag = 1000000
dist = -1
for i in range(3):
    xx, yy, mm = map(int, input().split())
    if mm < mag:
        mag = mm
        dist = (xx - x) ** 2 + (yy - y) ** 2
if dist < r * r:
    print("What a beauty!")
else:
    print("Time to move my telescope!")