n, m = map(int, input().split())
r = []
c = [""] * m

for _ in range(n):
    r.append("".join(input().split()))
    for i in range(m):
        c[i] += r[-1][i]

minx = m
maxx = 0
miny = n
maxy = 0

for i in range(n):
    firstx = r[i].find("*")
    if firstx != -1 and firstx < minx:
        minx = firstx
    lastx = r[i].rfind("*")
    if lastx != -1 and lastx > maxx:
        maxx = lastx

for i in range(m):
    firsty = c[i].find("*")
    if firsty != -1 and firsty < miny:
        miny = firsty
    lasty = c[i].rfind("*")
    if lasty != -1 and lasty > maxy:
        maxy = lasty

for i in range(miny, maxy + 1):
    print(" ".join(r[i][minx:maxx + 1]))
