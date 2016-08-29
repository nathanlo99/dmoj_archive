import itertools
m = list(map(int, input().split()))
crew = []
n = int(input())
for _ in range(n):
    crew.append(tuple(map(int, input().split())))

ans = 0
for i in itertools.combinations(range(n), min(n, 5)):
    sum_c = sum(crew[x][0] for x in i)
    sum_s = sum(crew[x][1] for x in i)
    sum_p = sum(crew[x][2] for x in i)
    ans = max(min((sum_c * 100) / m[0], (sum_s * 100) / m[1], (sum_p * 100) / m[2]), ans)
print("{:.1f}".format(min(100, ans)))