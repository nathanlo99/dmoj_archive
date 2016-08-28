n, k, t = map(int, input().split())
count = {}
names = ["aurpine", "kushanzaveri"]

times = [0, 0]
for i in map(int, input().split()):
    if i < k:
        count[i] = count.get(i, 0) + 1

for num in count:
    if num < k - num and k - num in count:
        pairs = min(count[num], count[k - num])
    elif num * 2 == k:
        pairs = count[num] // 2
    else:
        pairs = 0
    for i in range(pairs):
        times[t] += 1
        t = (t + 1) % 2

print(names[~t], times[~t])