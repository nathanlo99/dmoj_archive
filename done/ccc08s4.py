import sys
input = sys.stdin.readline

def solve_2(a, b):
    res = []
    for i in a:
        for j in b:
            res.append(i + j)
            res.append(i - j)
            res.append(j - i)
            res.append(i * j)
            if j != 0 and i % j == 0:
                res.append(i // j)
            if i != 0 and j % i == 0:
                res.append(j // i)
    return res

def solve_3(a, b, c):
    return solve_2(solve_2(a, b), c) + solve_2(solve_2(b, c), a) + solve_2(solve_2(c, a), b)

def solve_4(a, b, c, d):
    return solve_2(solve_3(a, b, c), d) + \
           solve_2(solve_3(b, c, d), a) + \
           solve_2(solve_3(c, d, a), b) + \
           solve_2(solve_3(d, a, b), c) + \
           solve_2(solve_2(a, b), solve_2(c, d)) + \
           solve_2(solve_2(b, c), solve_2(a, d))

n = int(input())
for i in xrange(n):
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    s = set(solve_4([a], [b], [c], [d]))
    ans = 0
    for i in s:
        if i <= 24 and i > ans:
            ans = i
    print(ans)