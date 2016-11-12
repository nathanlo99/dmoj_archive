import sys
input = sys.stdin.readline

numbers = [int(input()) for i in range(9)]
s = sum(numbers)
for i in range(9):
    for j in range(i + 1, 9):
        if s - numbers[i] - numbers[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(numbers[k])