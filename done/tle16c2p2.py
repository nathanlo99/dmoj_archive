n = int(input())
x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

max_ = 0
for xx, yy, zz in ((x, y, z), (x, z, y), (y, x, z), (y, z, x), (z, x, y), (z, y, x)):
    max_ = max(max_, (a // xx) * (b // yy) * (c // zz))

if max_ == 0:
    print("SCAMMED")
else:
    ans = n // max_
    if n % max_ != 0:
        ans += 1
    print(ans)