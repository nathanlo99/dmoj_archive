n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

ap = 0
bp = 0

a_ans = 0
b_ans = 0

while True:
    if ap >= n or bp >= n:
        break
    if a[ap] > b[bp]:
        a_ans += 1
        bp += 1
    ap += 1

ap = 0
bp = 0

while True:
    if ap >= n or bp >= n:
        break
    if b[bp] > a[ap]:
        b_ans += 1
        ap += 1
    bp += 1

print(a_ans)
print(b_ans)