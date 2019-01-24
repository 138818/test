import time

time_obj = time.time()
print(time_obj)

obj = time.localtime()
print(obj)
for item in obj:
    print(str(item))

ftime = time.asctime()
print(ftime)

dtime = time.strftime('%Y-%m-%d %H:%M:%S')
print(dtime)