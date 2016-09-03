n = int(input())
c = chr(ord('a') + n - 1)
s = c * (2 * n - 1)
l = 0
r = 2 * n - 1
stack = []
while r > l:
    s = s[:l] + c * (r - l) + s[r:]
    print(s)
    stack.append(s)
    l += 1
    r -= 1
    c = chr(ord(c) - 1)
stack.pop()
while stack:
    print(stack.pop())