import sys
a, b, c, d, s = map(int, sys.stdin.read().split('\n')[:-1])
x_pairs = (s // (a + b))
x_singles = min(a, s - x_pairs * (a + b))
y_pairs = (s // (c + d))
y_singles = min(c, s - y_pairs * (c + d))
x = x_pairs * (a - b) + x_singles
y = y_pairs * (c - d) + y_singles
print("Nikky" if x > y else ("Tied" if x == y else "Byron"))
