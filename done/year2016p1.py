s = []
for _ in range(int(input())): s += list(set(list(map(int, input().split()))[1:]))
print("YES" if len(list(s)) != len(set(s)) else "NO")