c, f, s = map(int, input().split())
for i in range(int(input())):
    t = input().split()
    xx, cc, ff, ss = map(int, t[0:4])
    if cc <= c * xx and ff <= f * xx and ss <= s * xx:
        print(" ".join(t[4:]))
