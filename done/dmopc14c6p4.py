n, m, h = map(int, input().split())
cars = [int(input()) for i in range(n)][::-1]

ans = 0
for i, v in enumerate(cars):
    if i == 0:
        continue
    # Brute force: this loop can be trivially optimized
    while cars[i - 1] - cars[i] > h:
        cars[i] += m
        ans += 1
print(ans)