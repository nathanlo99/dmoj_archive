import sys
input = sys.stdin.readline

n = int(input())
input()
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(n - len(a.intersection(b)))