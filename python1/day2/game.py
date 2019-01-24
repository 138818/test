import random
# computer = random.choice(["石头",  "剪刀", "布"])
# player = input('请输入(石头=1,剪刀=2,布=3): ')
# print('你出的的是:%s,电脑出的是:%s' % (player, computer))
# if player == "石头":
#     if computer == "石头":
#         print('\033[31;1m平局\033[0m')
#     elif computer == "剪刀":
#         print('\033[32;1m你赢了\033[0m')
#     else:
#         print('\033[31;1m你输了\033[0m')
# elif player == "剪刀":
#     if computer == "石头":
#         print('\033[31;1m你输了\033[0m')
#     elif computer == "剪刀":
#         print('\033[31;1m平局\033[0m')
#     else:
#         print('\033[32;1m你赢了\033[0m')
# else:
#     if computer == "石头":
#         print('\033[32;1m你赢了\033[0m')
#     elif computer == "剪刀":
#         print('\033[31;1m你输了\033[0m')
#     else:
#         print('\033[31;1m平局\033[0m')
####################################################
# all_choice = ['石头', '剪刀', '布']
# win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# show = """(0)石头
# (1)剪刀
# (2)布
# 请输入的选择:"""
# computer = random.choice(all_choice)
# player = int(input(show))
# print('你出的的是:%s,电脑出的是:%s' % (all_choice[player], computer))
# if all_choice[player] == computer:
#     print('\033[31;1m平局\033[0m')
# elif [all_choice[player], computer] in win_list:
#     print('\033[32;1m你赢了\033[0m')
# else:
#     print('\033[31;1m你输了\033[0m')
#########################################################
n = 1
r = {'c': 0, 'p': 0}
all_choice = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
show = """(0)石头
(1)剪刀
(2)布
请输入的选择:"""
while n < 4:
    computer = random.choice(all_choice)
    player = int(input(show))
    print('第%s局:你出的的是:%s,电脑出的是:%s' % (n, all_choice[player], computer))
    print('********************************')
    if all_choice[player] == computer:
        print('')
        # r['c'] = int(r['c']) + 1
        # r['p'] = int(r['p']) + 1
    elif [all_choice[player], computer] in win_list:
        r['p'] = int(r['p']) + 1
    else:
        r['c'] = int(r['c']) + 1
    n += 1

if int(r['c']) == int(r['p']):
    print('\033[31;1m结果: 平局\033[0m')
elif int(r['c']) > int(r['p']):
    print('\033[31;1m结果: 你输了\033[0m')
else:
    print('\033[32;1m结果: 你赢了\033[0m')


