import math

for _ in range(5):
    x1, y1, x2, y2 = map(int, input().split())
    angle1 = math.degrees(math.atan2(y1, x1))
    angle2 = math.degrees(math.atan2(y2, x2))
    diff = (angle1 - angle2 + 720.0) % 360.0
    print("{:.1f}".format(diff))