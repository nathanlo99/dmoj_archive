s = input().split(":")
a = int(s[0]) * 60 + int(s[1])

t = 120
while t > 0:
    if a < 420:
        d = min(t, 420 - a)
        t -= d
        a += d
    elif a < 600:
        d = min(t, (600 - a) // 2)
        t -= d
        a += d * 2
    elif a < 900:
        d = min(t, 900 - a)
        t -= d
        a += d
    elif a < 1140:
        d = min(t, (1140 - a) // 2)
        t -= d
        a += d * 2
    else:
        a -= 24 * 60
if a < 0:
    a += 24 * 60
print("{:02}:{:02}".format(a // 60, a % 60))