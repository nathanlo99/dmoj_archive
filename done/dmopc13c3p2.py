import sys
import datetime
input = sys.stdin.readline

n = int(input())
ymd, hms = input().split()
y, mon, d = map(int, ymd.split("/"))
h, m, s = map(int, hms.split(":"))

current = datetime.datetime(year=y, month=mon, day=d, hour=h, minute=m, second=s)
change = datetime.timedelta(hours=n)
print((current - change).strftime("%Y/%m/%d %H:%M:%S"))