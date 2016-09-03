from math import sin, cos, sqrt

n = int(input())
for _ in range(n):
    x, y, z, u, v, w, t = map(float, input().split())
    d = u * u + v * v + w * w
    k = (u * x + v * y + w * z) * (1 - cos(t))
    fx = (u * k + d * x * cos(t) + sqrt(d) * (-w * y + v * z) * sin(t)) / d
    fy = (v * k + d * y * cos(t) + sqrt(d) * (w * x - u * z) * sin(t)) / d
    fz = (w * k + d * z * cos(t) + sqrt(d) * (-v * x + u * y) * sin(t)) / d
    print("%.6f %.6f %.6f" % (fx, fy, fz))