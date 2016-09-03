a, b = int(input()), int(input())
c = 1
while min(a, b) >= 0:
  c += 1
  a, b = b, a - b
print(c)
