import sys
input = sys.stdin.readline

n = int(input())
day = 0
max_v = 0
value = 0

for i in xrange(1, n + 1):
    s = input().split()
    if s[0] == "borrow":
        value += int(s[1])
        if value > max_v:
            max_v = value
            day = i
    else:
        value -= int(s[1])
    
print(day)