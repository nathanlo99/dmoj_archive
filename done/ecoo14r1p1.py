a = (24. * 60. + 37. + 22.663 / 60.0) / (24. * 60.)

for i in range(10):
    d, h, m = map(int, input().split())
    earth_minutes = (d - 1) * 24 * 60 + h * 60 + m
    mars_minutes = earth_minutes / a
    md = int(mars_minutes // (24 * 60)) + 1
    mars_minutes %= 24 * 60
    mh = int(mars_minutes // 60)
    mars_minutes %= 60
    mm = int(mars_minutes)
    print("Day {}, {:02}:{:02}".format(md, mh, mm))