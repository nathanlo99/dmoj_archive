while True:
    n = int(input())
    if n == 0:
        break
    m = [[-1 for i in range(n + 1)]]
    for row in range(n):
        m.append([-1] + list(map(int, input().split())))
    # Identify Identity
    ident = set(range(1, n + 1))
    flag = True
    for i in range(1, n + 1):
        if not flag:
            break
        for j in set(ident):
            if not flag:
                break
            if m[i][j] != i:
                ident.remove(j)
                if len(ident) == 0:
                    flag = False
    if len(ident) != 1 or not flag:
        print("no")
        continue
    ident = ident.pop()
    # Checking inverses
    for i in range(1, n + 1):
        if not flag:
            break
        for j in range(1, n + 1):
            if m[i][j] == ident:
                break
        else:
            flag = False
    if not flag:
        print("no")
        continue
    # Checking associativity
    for i in range(1, n + 1):
        if not flag:
            break
        for j in range(i, n + 1):
            if not flag:
                break
            for k in range(j, n + 1):
                if m[m[i][j]][k] != m[i][m[j][k]]:
                    flag = False
    if not flag:
        print("no")
        continue
    print("yes")