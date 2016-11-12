n = int(input()) * 2
for i in range(int(input())):
    k = int(input())
    if k == 1:
        n -= 1
    elif k == 2:
        n -= 2
    else:
        n -= 10

if n < 0:
    print("Return")
else:
    print("Continue")