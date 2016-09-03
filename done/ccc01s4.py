points = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

min_diam = 1000000
for a in range(n):
    ax, ay = points[a]
    for b in range(a + 1, n):
        bx, by = points[b]
        center = (ax + bx) / 2.0, (ay + by) / 2.0
        ab = dist(points[a], points[b])
        radius = 0.5 * ab
        for point in points:
            if dist(center, point) > radius:
                break
        else:
            if radius * 2 < min_diam:
                min_diam = radius * 2

        for c in range(b + 1, n):
            cx, cy = points[c]
            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if d == 0:
                continue
            ux = ((ax ** 2 + ay ** 2) * (by - cy) + (bx ** 2 + by ** 2) * (cy - ay) + (cx ** 2 + cy ** 2) * (ay - by)) / d
            uy = ((ax ** 2 + ay ** 2) * (cx - bx) + (bx ** 2 + by ** 2) * (ax - cx) + (cx ** 2 + cy ** 2) * (bx - ax)) / d
            r = dist((ux, uy), points[a])
            for point in points:
                if dist(point, (ux, uy)) > r:
                    break
            else:
                if r * 2 < min_diam:
                    min_diam = r * 2

print("{:.2f}".format(min_diam))