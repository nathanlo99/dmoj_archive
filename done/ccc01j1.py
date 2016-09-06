n = int(input())
for i in range(1, n + 2, 2):
    print("*" * i + " " * (2 * n - 2 * i) + "*" * i)
for i in range(n - 2, 0, -2):
    print("*" * i + " " * (2 * n - 2 * i) + "*" * i)