n, k = map(int, input().split())

ans = [0] + [0] * (n - 2) + [k]
print(" ".join(map(str, ans)))