d = list(map(int, input().split()))
r = list(map(int, input().split()))

donors = [
    [0],
    [1, 0],
    [2, 0],
    [1, 2, 3, 0],
    [4, 0],
    [1, 4, 5, 0],
    [2, 4, 6, 0],
    [1, 2, 3, 4, 5, 6, 7, 0]
]

types = ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]

ans = 0

for i in [0, 1, 2, 4, 3, 5, 6, 7]:
    for j in donors[i]:
        p = min(d[j], r[i])
        if p == 0:
            continue
        d[j] -= p
        r[i] -= p
        #print("{} Type {} patients receive Type {} blood".format(p, types[i], types[j]))
        ans += p

print(ans)