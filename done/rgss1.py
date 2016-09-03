a, b, c = map(int, input().split())
print(max(i * a + ((c - i * a) // b) * b for i in range(c // a + 1)))