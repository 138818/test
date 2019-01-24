import getpass
import random
import string
import shutil
import os

########生成随机密码#####################
# all_chs = string.digits+string.ascii_letters
# def ran_pass(n=8):
#     result = ''
#     for ch in range(n):
#         result += random.choice(all_chs)
#     return result

# if __name__ == '__main__':
#     print(ran_pass(8))

########拷贝文件########################
# f1 = open('/etc/hosts')
# f2 = open('/tmp/zj', 'w')
# shutil.copyfileobj(f1, f2)
# f1.close()
# f2.close()

# shutil.copyfile('/etc/hosts', '/tmp/zj2')
###################################################
# for ind in [0,1,2,3,4]:
#     print('%s: %s' % (ind, alist[ind]))
#
# for ind in range(5):
#     print('%s: %s' % (ind, alist[ind]))
#
# for ind in range(len(alist)):   #常用
#     print('%s: %s' % (ind, alist[ind]))
#
# print(enumerate(alist))  #返回一个enumerate对象
# print(list(enumerate(alist)))  #将enumerate对象转换成列表以便进行分析
#
# for item in enumerate(alist):
#     print('%s: %s' % item)
#
# for ind, val in enumerate(alist):   #常用
#     print('%s: %s' % (ind, val))
#######################################################

def get_ball():
    ball = []
    while True:
        rballs = [random.randint(1, 33) for i in range(6)]
        rballs = list(set(rballs))
        rballs = sorted(rballs)
        if len(rballs) == 6:
            bball = [random.randint(1, 16)]
            ball.append(rballs)
            ball.append(bball)
            break
    return ball

def tongji(num=5):
    all_ball = []
    for i in range(5):
        all_ball.append(get_ball())  #[[[23,12,9],[5]],[[12,32,7,9],[5]]]




