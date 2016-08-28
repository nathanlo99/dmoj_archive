n = int(input())
cuteness = list(map(int, input().split()))

probs = []
start = 0
for _ in range(n):
    i, p, s, t = map(int, input().split())
    start = max(s, start)
    probs.append((i, p, t))

for i, p, t in probs:
    if p == 10:
        print(0)
    elif t * cuteness[i - 1] + start <= 180:
        print(10 - p)
    else:
        print("The kemonomimi are too cute!")