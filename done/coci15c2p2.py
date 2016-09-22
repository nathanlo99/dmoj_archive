n, m = map(int, input().split())
r = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    r[a].append(b)
    r[b].append(a)

def count(available, so_far):
    res = 1
    start = 1 if len(so_far) == 0 else so_far[-1] + 1
    for i in range(start, n + 1):
        if i in available:
            new_available = available.copy()
            for j in r[i]:
                if j in new_available:
                    new_available.remove(j)
            res += count(new_available, so_far + [i])
    return res

print(count(list(range(1, n + 1)), [0]))