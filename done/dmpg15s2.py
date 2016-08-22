r, n = map(int, input().split())
to_unlock = []
unlocked = []
for _ in range(r):
    x, y, w, l = map(int, input().split())
    to_unlock.append((x, y, w, l))
for _ in range(n):
    mx, my = map(int, input().split())
    for i, (x, y, w, l) in enumerate(to_unlock):
        if i in unlocked:
            continue
        if x <= mx < x + w and y <= my < y + l:
            unlocked.append(i)
print(len(unlocked))