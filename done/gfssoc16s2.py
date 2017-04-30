import itertools
import bisect

a = []
for i in range(1, 9):
    a += list(int("".join(x), 16) for x in itertools.product("ACE", repeat=i))

x = int(input())
y = int(input())

print(bisect.bisect_right(a, y) - bisect.bisect_left(a, x))