s = input()
r1, g1, b1 = map(float, input().split())
r2, g2, b2 = map(float, input().split())

mul = lambda x, y: x*y
scr = lambda x, y: 1-(1-x)*(1-y)
ovr = lambda x, y: 1-2*(1-x)*(1-y) if x >= 0.5 else 2*x*y

if s == "Multiply":
    f = mul
elif s == "Screen":
    f = scr
else:
    f = ovr

print(f(r1, r2), f(g1, g2), f(b1, b2))