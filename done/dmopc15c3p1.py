a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a == c and b == d):
    print("YES")
elif (a == b or c == d):
    print("NO")
else:
    print("YES" if (a < c < b) or (a < d < b) or (c < a < d) or (c < b < d) else "NO")