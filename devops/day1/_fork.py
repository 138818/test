import os

# print('hello world')
# obj = os.fork()
# if obj:
#     print('parnt')
# else:
#     print('child')
#
# print('hao are your')

################
for i in range(3):
    obj = os.fork()
    if not obj:
        print('hello')
        exit()