# 10
# 3
# 4
# 6
# 2

n = int(input())
k = int(input())
print((k + 1) * n - sum([int(input()) for i in range(k)]))