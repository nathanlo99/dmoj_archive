n = int(input())
best_m, best_o = map(int, input().split())
worst_m, worst_o = best_m, best_o

for i in range(n - 2):
    on, off = map(int, input().split())
    # Worst case: most of the people getting off got on at M
    a = min(off, worst_m)
    worst_m -= a
    worst_o -= off - a

    # Best case: not many people getting off got on at M
    b = min(off, best_o)
    best_o -= b
    best_m -= off - b

    worst_o += on
    best_o += on

print(worst_m)
print(best_m)