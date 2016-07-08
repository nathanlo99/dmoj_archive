r = []
for i in range(int(input())): r.append(tuple(input().split()))
r.sort(reverse=True, key=lambda x:x[0])
r.sort(key=lambda x: 2 * int(x[1]) + 3 * int(x[2]) + int(x[3]))
if len(r) >= 1: print(r[-1][0])
if len(r) >= 2: print(r[-2][0])
