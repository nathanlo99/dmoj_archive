import itertools

for _ in range(int(input())):
    a = int(input())
    b = int(input())
    c = int(input())
    aa = [input() for i in range(a)]
    bb = [input() for i in range(b)]
    cc = [input() for i in range(c)]
    for a in aa:
        for b in bb:
            for c in cc:
                print(a, b, c, end=".\n")
    print()