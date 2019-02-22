import time


t = (2020, 2, 15, 10, 13, 38, 1, 48, 0)

d = time.mktime(t)
print('mktime:', d)

# convertendo em asc
print('asctime: ', time.asctime(time.localtime(d)))
