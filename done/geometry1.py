for _ in range(int(input())):
    ax, ay, bx, by, cx, cy = map(int, input().split())
    ab = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
    bc = ((bx - cx) ** 2 + (by - cy) ** 2) ** 0.5
    ac = ((ax - cx) ** 2 + (ay - cy) ** 2) ** 0.5
    s = (ab + bc + ac) / 2.0
    area = (s * (s - ab) * (s - bc) * (s - ac)) ** 0.5
    perim = ab + bc + ac
    print("{:.2f} {:.2f}".format(area, perim))