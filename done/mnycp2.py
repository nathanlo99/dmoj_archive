from math import log, ceil
t_days = ceil(log(float(input()) / 2.0, 2) * 2 * 365)

years = int(t_days // 365)
t_days %= 365
months = int(t_days // 30)
t_days %= 30
weeks = int(t_days // 7)
t_days %= 7
days = int(t_days)

if max(years, months, weeks, days) == 0:
    print("Now!")
else:
    if years > 0:
        print("{}Y".format(years), end=" ")
    if months > 0:
        print("{}M".format(months), end=" ")
    if weeks > 0:
        print("{}W".format(weeks), end=" ")
    if days > 0:
        print("{}D".format(days), end=" ")
    print()