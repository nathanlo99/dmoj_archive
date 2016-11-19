menu = [[-1, 461, 431, 420, 0],[-1, 100, 57, 70, 0],[-1, 130, 160, 118, 0],[-1, 167, 266, 75, 0]]

total = sum(menu[_][int(input())] for _ in range(4))
print("Your total Calorie count is", str(total) + ".")