N, L, R = map(int, input().split())
print(sum(sorted(map(int, input().split()), reverse=True)[R-1::L]))
