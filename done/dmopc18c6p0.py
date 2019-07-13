t = list(map(int, input().split()))

zero = sum(1 for x in t if x == 0)
if zero == 0:
    print("NO")
elif zero == 1:
    print("NO" if ((t[0] == 0 and t[1] == 3 and t[2] == 2) or (t[1] == 0 and t[2] == 1 and t[0] == 3) or (t[2] == 0 and t[0] == 2 and t[1] == 1)) else "YES")
elif zero >= 2:
    print("YES")