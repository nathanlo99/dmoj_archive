import itertools
presents = []
total_w = 0
n = int(input())
for _ in range(n):
    f, w = map(int, input().split())
    total_w += w
    presents.append((w, f))

min_ans = 1000000000000

for order in itertools.permutations(range(n), n):
    ans = 0
    h = 101
    t = total_w
    for i in order:
        w, f = presents[i]
        ans += t * (abs(h - f) + 1)
        t -= w
        h = f
    if ans < min_ans:
        min_ans = ans

print(min_ans)