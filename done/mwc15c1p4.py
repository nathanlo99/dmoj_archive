def prob(a, b, c):
    ans = 0
    a0 = int(ord(a[0]) >= ord('a'))
    a1 = int(ord(a[1]) >= ord('a'))
    b0 = int(ord(b[0]) >= ord('a'))
    b1 = int(ord(b[1]) >= ord('a'))
    c = int(ord(c[0]) >= ord('a')) + int(ord(c[1]) >= ord('a'))
    for i in [a0 + b0, a0 + b1, a1 + b0, a1 + b1]:
        if i == c:
            ans += 1
    return ans / 4.
    

n = int(input())
a = input()
b = input()
c = input()

ans = 1.0
for i in range(0, 2 * n, 2):
    ans *= prob(a[i: i + 2], b[i: i + 2], c[i: i + 2])
print("{:.6f}".format(ans))
