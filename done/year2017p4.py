import sys
input = sys.stdin.readline

rules = {}
for _ in range(int(input())):
    rule = input()
    reactants, product = rule.split("=")
    reactants = tuple(sorted(
        x for x in reactants.split(" ") if x not in ("", "(", "+", ")")))
    rules[reactants] = product.strip()

for _ in range(int(input())):
    stack = []
    for token in input().split():
        if token == "+":
            continue
        elif token == ")":
            p = len(stack) - 1
            while stack[p] != "(":
                p -= 1
            stack = stack[:p] + [rules[tuple(sorted(stack[p + 1:]))]]
        else:
            stack.append(token)
    print(stack[0])