import sys
input = sys.stdin.readline

def fib(n):
  if not n: return (0, 1)
  else:
    a, b = fib(n // 2)
    e = a * a
    c = 2 * b * a - e
    d = e + b * b
    if not n & 1: return (c % 1000000007, d % 1000000007)
    else: return (d % 1000000007, (c + d) % 1000000007)

print(fib(int(input()))[0])