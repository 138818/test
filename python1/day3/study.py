import random

# def say():
#     print('hello world!')
# say()
######################################
# def guess():
#     while True:
#         random_number = random.randint(1, 100)
#         answer = int(input('猜100以内的数字: '))
#         if random_number > answer:
#             print('小了!')
#         elif random_number < answer:
#             print('大了!')
#         else:
#             print('恭喜你,猜对了!')
#             break
# guess()
############################################################
# num1 = int(input('one number: '))
# num2 = int(input('two number: '))
# num3 = int(input('three number: '))
# temp = 0
# if num1 > num2:
#     temp = num1
#     num1 = num2
#     num2 = temp
# if num2 > num3:
#     num2 = num3
#     num3 = temp
# print(num1,'',num2,'',num3)
###############################################################
# game = ('石头', '剪刀', '布')
# win = [{'石头': '剪刀'}, {'剪刀': '布'}, {'布': '布'}]
# info = '''0)石头
# 1)剪刀
# 2)布
# 请出拳:
# '''
# num = ('0', '1', '2')
# while True:
#     pinput = input(info)
#     if pinput not in num:
#         break
#     computer = game[random.randint(0, 2)]
#     player = game[int(pinput)]
#     if computer == player:
#         print('平局!')
#     elif player in win:
#         print('玩家赢!')
#     else:
#         print('电脑赢!')
#     print('*' * 10)
###################################################################
# for a in range(1, 10):
#     for b in range(1,a+1):
#         print('%s X %s = %s' % (a, b, a*b), end='\t')
#     print('')

##########################################################
# name = ['小名', '西门庆', '武松', '宋江', '林冲', '张三丰', '赵云', '吕布', '秦始皇', '刘备']
# num = random.randint(1, 10)
# print(name[num])

###########################################################
# sum = 0
# zheng = 0
# dan = 0
# for i in range(100):
#     if i % 2 == 0:
#        zheng += i
#     else:
#         dan += i
#     sum += i
# print(sum, zheng, dan)

###########################################################
def fuhao(fh):
    for i in range(3):
        print('%s' % fh * 5, end='')
for a in range(8):
    for b in range(8):
        if b % 2 == 0:
            fuhao('*')
        else:
            fuhao('#')
    print('')

