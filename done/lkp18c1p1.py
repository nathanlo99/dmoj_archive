n, k = map(int, input().split())
amts = sorted(list(map(int, input().split())), reverse=True)

cnt = 0
for amt in amts:
    if k >= amt:
        cnt += k // amt
        k -= (k // amt) * amt
if k == 0:
    print(cnt)
else:
    print(-1)