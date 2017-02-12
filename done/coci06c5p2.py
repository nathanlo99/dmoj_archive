h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))

h2 -= h1
m2 -= m1
s2 -= s1

if s2 < 0:
    s2 += 60
    m2 -= 1
if m2 < 0:
    m2 += 60
    h2 -= 1
if h2 < 0:
    h2 += 24
if max(s2, m2, h2) == 0:
    h2 = 24
print("{:02}:{:02}:{:02}".format(h2, m2, s2))