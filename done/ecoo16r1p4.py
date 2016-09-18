import sys
input = sys.stdin.readline

t_num = 10
h_num = 100

for _ in range(t_num):
    cx, cy = map(int, input().split())
    houses = []
    for __ in xrange(h_num):
        x, y, dr = input().split()
        houses.append((int(x), int(y), dr))
    total = 0
    total_d = 0
    for x in range(cx - 50, cx + 51):
        h = int((2500 - (cx - x) ** 2) ** 0.5) + 1
        for y in range(cy - h, cy + h + 1):
            if (cx - x) ** 2 + (cy - y) ** 2 > 50 ** 2:
                continue
            if (x, y, "R") in houses or (x, y, "D") in houses:
                continue
            total += 1
            houses.sort(key=lambda e: (x - e[0]) ** 2 + (y - e[1]) ** 2)
            votes = ""
            for i in xrange(3):
                votes += houses[i][2]
            
            p = 3
            dist = (x - houses[2][0]) ** 2 + (y - houses[2][1]) ** 2
            while p < h_num and (x - houses[p][0]) ** 2 + (y - houses[p][1]) ** 2 == dist:
                votes += houses[p][2]
                p += 1
                
            if votes.count("D") >= votes.count("R"):
                total_d += 1
    print("{:.01f}".format(100.0 * total_d / total))