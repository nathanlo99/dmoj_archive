from math import sqrt

d = int(input())
while(d):
    for i in range(int(sqrt(d)), 0, -1):
        if d % i == 0:
            print("Minimum perimeter is", 2 * (i + d // i), "with dimensions", i, "x", d // i)
            break
    d = int(input())
