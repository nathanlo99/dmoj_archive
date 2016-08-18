n, k = map(int, input().split())
t = []
for i in range(n):
    a = int(input())
    if a > 0:
        t.append(a)
print(sum(sorted(t)[-min(len(t), k):]))
