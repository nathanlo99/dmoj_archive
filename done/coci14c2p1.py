buttons = "22233344455566677778889999"
times = "12312312312312312341231234"
mapping = {}

c = 1
for i in input().split():
    mapping[i] = str(c)
    c += 1

actions = ""
for c in input():
    c = ord(c) - ord('a')
    button = buttons[c]
    time = int(times[c])
    if len(actions) > 0 and actions[-1] == button:
        actions += "#"
    actions += button * time
ans = ""
for action in actions:
    ans += mapping.get(action, action)
print(ans)