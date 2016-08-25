s, m, l = map(int, input().split())
a, b, c = map(lambda x: sum((int(a) * (100 ** (1 - i)) for i, a in enumerate(x.split(".")))), input().split())

ans = 0
orders = [a for i in range(s)] + [b for i in range(m)] + [c for i in range(l)]
while len(orders) >= 3:
    ans += orders[0] + orders[1] + orders[2]
    orders = orders[3:-1]
ans += sum(orders)
print("{}.{:02}".format(ans // 100, ans % 100))