while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    diff = [s[i + 1] - s[i] for i in range(1, len(s) - 1)]
    for i in range(1, len(diff) + 1):
        if all(diff[j] == diff[j + i] for j in range(0, len(diff) - i)):
            print(i)
            break
    else:
        print(len(diff))