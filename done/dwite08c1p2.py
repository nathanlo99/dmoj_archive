for _ in range(5):
    i, s = input().split()
    while len(i) != 1:
        i = str(sum(map(int, list(i))))
    print("match" if ord(s) - ord('A') == int(i) - 1 else "error")