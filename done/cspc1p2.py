n = int(input())
w = int(input())
h = int(input()) if w > 0 else 0

print("It takes {} hours for Team 610 build a robot.".format(n * (w - 1) + (n + h) * (6 - w + 1)))
