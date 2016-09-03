import sys
input = sys.stdin.readline

for _ in xrange(int(input())):
    n = int(input())
    d = [int(input()) for i in xrange(n)]
    next_item = 1
    stack = []
    while d:
        a = d.pop()
        if a == next_item:
            next_item += 1
        else:
            stack.append(a)
        while stack != [] and stack[-1] == next_item:
            stack.pop()
            next_item += 1

    print("Y" if sorted(stack) == stack else "N")