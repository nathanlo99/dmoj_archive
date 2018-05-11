qs = [""] * 5
for _ in range(5):
    q = input()
    n = int(input())
    qs[n-1] = q
print("\n".join(qs))