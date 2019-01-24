
#
# try:
#     num = int(input('number: '))
#     result = 100 / num
# except (ValueError, ZeroDivisionError):
#     print('Invalid input')
# except (EOFError, KeyboardInterrupt):
#     print('程序异常退出')
# else:
#     print(result)
# finally:
#     print('Done')



# def set_age1(name, age):
#     if not 1<age<120:
#         raise ValueError('超范围')
#     print('%s is old %s' % (name, age))
#
# def set_age2(name,age):
#     assert 1 < age < 120, '超范围'
#     print('%s is old %s' % (name, age))
#
# if __name__ == '__main__':
#     set_age2('tom', 220)
#
# import pickle
# #
# # fobj = open('/tmp/data', 'wb')
# # mylist = ['age', 'apple']
# # pickle.dump(mylist, fobj)
# # fobj.close()
#
# with open('/tmp/data', 'rb') as fobj:
#     mylist = pickle.load(fobj)
#     print(type(mylist))
# print(mylist)
# print(mylist[1])

# import os
# print(os.getcwd())
# os.chdir('/tmp')
# print(os.getcwd())
# # os.mkdir('/tmp/wjy')
# os.chdir('/tmp/wjy')
# print(os.getcwd())
# # os.mknod('h1.txt')
# print(os.listdir('/tmp/wjy'))
# os.chmod('/tmp/wjy/h1.txt', 0o600)
# print(os.path.basename('/tmp/wjy/h1.tt'))
# print(os.path.dirname('/tmp/wjy/h1.txt'))
# print(os.path.split('/tmp/wjy/hi.txt'))
# print(os.path.join('/tmp/wjy','h1.txt'))
# print(os.path.getsize('/tmp/wjy/h1.txt'))

import hashlib

md = hashlib.md5()
md.update('admin'.encode('utf-8'))

print(md.hexdigest())