import sys
input = sys.stdin.readline

n = int(input())
running = set()
for _ in range(2 * n - 1):
    running.symmetric_difference_update({input()})
print(running.pop())