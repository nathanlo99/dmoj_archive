h, m = map(int, input().split())
x = int(input())
m += x
h += m // 60
print("{} {}".format(h % 24, m % 60))
