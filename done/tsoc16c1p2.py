s = input()
if "." not in s:
    filename = s
    ext = input().lower()
else:
    filename, ext = s.split('.')
print("\"{}\" - {}".format(filename, ext))