k = int(input())
prices = list(map(int, input().split()))
x = int(input())
menu = list(map(int, input().split()))
t = int(input())
meals = sorted(map(int, input().split()))

ans = 0
menu_items = {}
for meal in meals:
    if meal not in menu:
        ans += prices[meal - 1]
    else:
        menu_items[meal] = menu_items.get(meal, 0) + 1

while True:
    current = []
    for menu_item in menu:
        amount = menu_items.get(menu_item, 0)
        if amount > 0:
            current.append(menu_item)
            menu_items[menu_item] = amount - 1
    ans += min((sum(prices[item - 1] for item in current), x))
    if len(current) == 0:
        break

print(ans)