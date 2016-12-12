n, a, b = map(int, input().split())
for _ in range(n):
    print("DA" if int(input()) ** 2 <= a * a + b * b else "NE")