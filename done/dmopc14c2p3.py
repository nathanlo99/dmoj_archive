_ = input()
print(sum(a * b for (a, b) in zip(sorted(list(map(int, input().split()))), sorted(list(map(int, input().split())), reverse=True))))
