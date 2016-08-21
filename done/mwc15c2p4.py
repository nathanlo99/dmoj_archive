import sys
input = sys.stdin.readline
input()
n = sorted(map(int, input().split()))
total = 0
p = None
while n:
    num = n.pop()
    if n[-1] == num:
        if p is not None:
            total += p * num
            p = None
        else:
            p = num
        n.pop()
    elif n[-1] == num - 1:
        if p is not None:
            total += p * (num - 1)
            p = None
        else:
            p = num - 1
        n.pop()
print(total)
