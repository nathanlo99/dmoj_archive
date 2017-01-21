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
    recipe = input()
    stack = []
    tokens = [x for x in recipe.split() if x != "+"]
    for token in tokens:
        if token != ")":
            stack.append(token)
        else:
            p = len(stack) - 1
            while stack[p] != "(":
                p -= 1
            stack, ingredients = stack[:p], stack[p + 1:]
            product = rules[tuple(sorted(ingredients))]
            stack.append(product)
    print(stack[0])