n = int(input())
slides = {}
paths = {1: 1}
x, y = map(int, input().split())
while x > 0:
    slides[y] = slides.get(y, []) + [x]
    x, y = map(int, input().split())
for i in range(2, n + 1):
    paths[i] = sum(paths[j] for j in slides.get(i, []))
print(paths[n])
