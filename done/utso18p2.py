a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

sm = 0
if b[1] == a[0] and c[1] > 0:
    sm += c[1]
if b[2] == a[1] and c[2] > 0:
    sm += c[2]
if b[0] == a[2] and c[0] > 0:
    sm += c[0]
print(sm)