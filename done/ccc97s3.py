for _ in range(int(input())):
    n = int(input())
    t0, t1, t2 = n, 0, 0
    c = 0
    while True:
        print("Round {}: {} undefeated, {} one-loss, {} eliminated".format(
                c, t0, t1, t2))
        if t0 + t1 == 2:
            if t0 == 2:
                t0 -= 1
                t1 += 1
            elif t0 == 1:
                t0 -= 1
                t1 += 1
            else:
                t1 -= 1
                t2 += 1
        elif t0 + t1 == 1:
            break
        else:
            num_t1 = t1 // 2
            t1 -= num_t1
            t2 += num_t1
            num_t0 = t0 // 2
            t0 -= num_t0
            t1 += num_t0
        c += 1
    print("There are {} rounds.\n".format(c))