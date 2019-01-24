import os
import time

# print('start.....')
# ret_val = os.fork()
# if ret_val:
#     print('parent sleep....')
#     time.sleep(20)
#     result = os.waitpid(-1, 0)
#     print(result)
#     time.sleep(10)
#     print('parent done')
# else:
#     print('child sleep ...')
#     time.sleep(30)
#     print('child done')


print('start.....')
ret_val = os.fork()
if ret_val:
    print('parent sleep....')
    time.sleep(20)
    result = os.waitpid(-1, 1)
    print(result)
    time.sleep(10)
    print('parent done')
else:
    print('child sleep ...')
    time.sleep(20)
    print('child done')