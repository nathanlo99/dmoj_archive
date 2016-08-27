time = 0

last_sent = {}
total_waiting = {}
replied = {}

for _ in range(int(input())):
    code, num = input().split()
    num = int(num)
    if code == "R":
        last_sent[num] = time
        replied[num] = False
    elif code == "S":
        wait = time - last_sent[num]
        total_waiting[num] = total_waiting.get(num, 0) + wait
        replied[num] = True
    elif code == "W":
        time += num - 2
    time += 1

for friend in sorted(last_sent.keys()):
    if not replied[friend]:
        print("{} -1".format(friend))
    else:
        print("{} {}".format(friend, total_waiting.get(friend, -1)))