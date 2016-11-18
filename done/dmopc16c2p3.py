for _ in range(int(input())):
    n, m = map(int, input().split())
    print((lambda a: ("a" * a + "b" * (n - a))) (max(int(input().split()[0]) for _ in range(m))))