for _ in range(int(input())):
    n = int(input())
    sums = set()
    diff = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sums.add(i + n // i)
            diff.add(n // i - i)
    done = False
    for s in sums:
        if s in diff:
            done = True
            print("{} is nasty".format(n))
            break
    if done:
        continue
    for d in diff:
        if d in sums:
            done = True
            print("{} is nasty".format(n))
            break
    if done:
        continue
    print("{} is not nasty".format(n))