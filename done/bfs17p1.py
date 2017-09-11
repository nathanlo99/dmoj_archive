input()
s = list(input().split())
print(sum(1 for i in s if len(i) <= 10))