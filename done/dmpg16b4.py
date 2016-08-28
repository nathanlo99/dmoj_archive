def f(n):
    return sum(int(c) ** len(str(n)) for c in str(n))

for _ in range(int(input())):
    n = int(input())
    visited = [n]
    while True:
        fn = f(n)
        if fn in visited:
            if fn == n:
                print("Equilibrium: Bob's investment becomes ${} after {} second(s)!".format(
                    fn, len(visited) - 1))
                break
            else:
                first = visited.index(fn)
                cycle = len(visited) - first
                print("Instability: Loop of length {} encountered after {} second(s)!".format(cycle, first))
                break
        visited.append(fn)
        n = fn