d = int(input())
e = int(input())
w = int(input())

a = max(0, d - 100) * 25 + 15 * e + 20 * w
b = max(0, d - 250) * 45 + 35 * e + 25 * w

print("Plan A costs", str(a//100) + "." + str(a % 100))
print("Plan B costs", str(b//100) + "." + str(b % 100))

if a < b: print("Plan A is cheapest.")
elif b < a: print("Plan B is cheapest.")
else: print("Plan A and B are the same price.")