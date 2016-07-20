n = int(input())
k = list(map(int, input().split()))
last = 1
best = 1
for i, v in enumerate(k):
    if i + 1 < n and abs(k[i + 1] - v) <= 2: last += 1
    else: last = 1
    best = max(best, last)
print(best)
