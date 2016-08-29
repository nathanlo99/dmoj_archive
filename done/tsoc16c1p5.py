n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i

for _ in range(int(input())):
    poss = list(range(1, n + 1))
    q = int(input())
    f = fact
    for i in range(n, 0, -1):
        f //= i
        j = q // f
        print(poss[j], end=" ")
        poss.remove(poss[j])
        q %= f
    print()