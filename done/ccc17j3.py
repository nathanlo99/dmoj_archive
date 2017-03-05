a, b = map(int, input().split())
c, d = map(int, input().split())
n = int(input())
print("Y" if (n - (a - c) - (b - d)) % 2 == 0 and (n >= abs(a - c) + abs(b - d)) else "N")