s = input()
state = [1, 2, 3, 4]

def v():
    global state
    state = [state[1], state[0], state[3], state[2]]

def h():
    global state
    state = [state[2], state[3], state[0], state[1]]

for c in s:
    if c == "H":
        h()
    else:
        v()

print(state[0], state[1])
print(state[2], state[3])