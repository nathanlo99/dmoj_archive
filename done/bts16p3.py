import sys
input = sys.stdin.readline

n = int(input())
last = ""
last_value = 1
ans = 0
for i, name in enumerate(input().split()):
    if name[0] == last:
        last_value += 1
        ans += last_value
    else:
        ans += 1
        last_value = 1
    last = name[0]
print(ans)