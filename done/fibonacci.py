import sys
input = sys.stdin.readline

def fib(n):
  if not n: return (0, 1)
  else:
    a, b = fib(n // 2)
    if not n & 1: return ((2 * b * a - a * a) % 1000000007, (a * a + b * b) % 1000000007)
    else: return ((a * a + b * b) % 1000000007, (2 * b * a + b * b) % 1000000007)

print(fib(int(input()))[0])