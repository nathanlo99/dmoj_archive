g = int(input())
for _ in range(g):
    n = int(input())
    attack = list(map(int, input().split()))
    health, taunt = map(int, input().split())
    for i in range(2 ** n):
        h = health
        t = taunt
        for j in range(n):
            if ((i >> j) & 1) != 0:
                h -= attack[j]
            else:
                t -= attack[j]
        if h <= 0 and t <= 0:
            print("LETHAL")
            break
    else:
        print("NOT LETHAL")