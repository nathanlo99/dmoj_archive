buttons = "22233344455566677778889999"
times = "12312312312312312341231234"

while 1:
    s = input()
    if s == "halt":
        break
    count = 0
    last_button = "0"
    # actions = []
    for c in s:
        c_ = ord(c) - ord('a')
        button = buttons[c_]
        time = int(times[c_])
        if button == last_button:
            count += 2
        # if len(actions) > 0 and actions[-1] == button:
        #     actions.append(" ")
        count += time
        last_button = button
        # for i in range(time):
        #     actions.append(button)
    print(count)