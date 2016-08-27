for _ in range(int(input())):
    n = int(input())
    m = list(map(int, input().split()))
    ans = 0
    for ptr in range(n):
        minimum = min(m[ptr:])
        index = m.index(minimum)
        ans += index - ptr
        m = m[:ptr] + [minimum] + m[ptr:index] + m[index+1:]
    print(ans)