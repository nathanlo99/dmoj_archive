import sys
import datetime

a, b = map(int, input().split())
c, d = map(int, input().split())
t = abs(d - b) + abs(c - a)

#YYYY:MM:DD:HH:MM:SS
start = input()
start_time = datetime.datetime.strptime(start, "%Y:%m:%d:%H:%M:%S")
time_delta = datetime.timedelta(seconds=t)
end_time = start_time + time_delta
print(end_time.strftime("%Y:%m:%d:%H:%M:%S"))