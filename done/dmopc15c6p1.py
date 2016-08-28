import sys
current, goal, bonus, experience, cost = map(int, sys.stdin.read().split('\n')[:-1])
needed = goal - current
cooked = 0
triple_bonus = bonus // experience
cooked += min(triple_bonus, needed // (3 * experience))
remaining_bonus = bonus - triple_bonus * experience
needed -= cooked * 3 * experience
if needed <= 0:
    print("{}\n{}".format(cooked, cooked * cost))
    sys.exit(0)
if needed >= 2 * experience + remaining_bonus:
    needed -= 2 * experience + remaining_bonus
    cooked += 1
if needed <= 0:
    print("{}\n{}".format(cooked, cooked * cost))
    sys.exit(0)
normal_fish = needed // (2 * experience)
cooked += normal_fish
needed -= normal_fish * 2 * experience
if needed > 0:
    cooked += 1
    needed -= 2 * experience
if cooked == 1024:
    cooked -= 1
print("{}\n{}".format(cooked, cooked * cost))