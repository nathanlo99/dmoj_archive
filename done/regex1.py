import re, datetime, sys

matches = re.findall(r'([0-9]{4})-([0-9]{2})-([0-9]{2})', sys.stdin.read())
for match in matches:
    year, month, day = map(int, match)
    try:
        datetime.datetime.strptime("-".join(match), "%Y-%m-%d")
    except ValueError:
        continue
    print("-".join(match))