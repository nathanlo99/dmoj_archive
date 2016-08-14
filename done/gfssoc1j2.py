import sys
input = sys.stdin.readline

x, y = 0, 0

for _ in range(int(input())):
    direction = input().rstrip()
    if direction == "North":
        y += int(input())
    elif direction == "South":
        y -= int(input())
    elif direction == "East":
        x += int(input())
    else:
        x -= int(input())
print(x, y)
