import os
import random
import keyword
import sys
import getpass
import shutil
import string
import subprocess

# def sayhi():
#     print('hello world!')
#
# if __name__ == '__main__':
#     sayhi()
#####################################################
# def rand_pass(num=6):
#     pass_chs = string.ascii_letters+string.digits
#     r_pass = ""
#     for ch in range(num):
#         r_pass += random.choice(pass_chs)
#     return r_pass
# if __name__ == '__main__':
#     print(rand_pass(8))
#########################################################
# def adduser(username,userpass,userfile):
#     f_info = """user_name: %s\nuser_pass: %s\n""" % (username, userpass)
#     subprocess.call('useradd %s' % username, shell=True)
#     subprocess.call('echo %s | passwd --stdin %s' % (userpass, username), shell=True)
#     with open(userfile, 'a') as fobj:
#         fobj.write(f_info)
# if __name__ == '__main__':
#     upass = rand_pass()
#     adduser(sys.argv[1], upass, '/tmp/user.info')
################################################################
# def grap(tx):
#     for a in range(3):
#         print('%s' % tx * 5)
#
# for a in range(8):
#     grap('@')
#####################################################
# def grap(x, y, g, t1, t2):
#     n = 1
#     c = 0
#     for a in range(y):
#         for a in range(g):
#             for b in range(int(x/g)):
#                 if n % 2 == 1:
#                     print(t1, end='')
#                 else:
#                     print(t2, end='')
#             n += 1
#         print('')
#         c += 1
#         if c % 3 == 0:
#             t1, t2 = t2, t1
# if __name__ == '__main__':
#     grap(40,24,8,'>','&')

#############################################################
# def run_nian(year):
#     if not year.isdigit():
#         return '输入有误!'
#     year = int(year)
#     if (year % 4 ==0 and year % 100 == 0) or (year % 400 == 0):
#         return '%s是润年' % str(year)
#     else:
#         return '%s是不是润年' % str(year)
#
# if __name__ == '__main__':
#     year = input('输入年份: ')
#     print(run_nian(year))
##############################################################
def char_type(chs):
    chs = chs.strip()
    if chs.isdigit():
        return '%s是数字' % chs
    else:
        return '%s不是数字' % chs

if __name__ == '__main__':
    print(char_type(input('请输入: ')))

######################################