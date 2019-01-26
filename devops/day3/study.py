import random
import getpass

# print('hello world')
# print('hello', 'world')
# print('hello' + 'world')
# print('hello' * 10)
# print('hello', 'world', sep='-')
# print(3 + 5)
# print(4 - 2)
# print(2 * 3)
# print(5 / 2)
# print(5 // 2)
# print(2**3)
# print(5 % 2)
# print(5 > 2)
# print(5 == 2)
# print(1 > 2 and 2 > 3)
# print(not 2 < 5)
#
# # num = input('input: ')
# # print(type(num))
# # print(num + str(10))
# # print(int(num)+20)
#
# strs = 'tom\'s not is cat'
# strs = "tom's not is cat"
# strs = "the book name is \"jianshu\""
#
# line = """
# 这是
# 换行
# ！
# """
# line = '''
# 这是
# 换行
# ！
# '''
#
# str_py = 'python'
# len(str_py)
# str_py[0]
# str_py[-1]
# str_py[1:]
# str_py[2:4]
# str_py[2:-1:2]
# str_py[1::2]
# str_py[::2]
# str_py[::-1]
# print(str_py * 3)
#
# 'to' in str_py
# 'py' not in str_py
#
#
# a = ['tom', 1, 'zhangsan', 3, [1, 2, 3]]
# len(a)
# a[-1][-1]
# [1, 2, 3][-1]
# a[2:3]
# 'a' in a
# 3 not in a
#
# a.append([4, 5, 6])
# a.append('lucy')
# a.append(10)
#
#
# auple = (1, 2, 3, 4, 5, 'a', 'b')
# len(auple)
# 10 in auple
# auple[2]
# auple[3:5]
#
# b = {'name': 'tom', 'age': 18}
# print(len(b))
# print('bob' in b)
# b['age']=25
# b['addr'] = 'zhe li'
# print(b['addr'])
#
# if 3 > 0:
#     print('yes')
# else:
#     print('no')
#
# if 2 in auple:
#     print('yes')
#
# if -0.0:
#     pass
# if []:
#     print('[]')
# if {}:
#     print('[]')
# if ():
#     print('[]')
# if ' ':
#     print('null')
# a = 3;b = 1
# s = a if a > b else b
# print(s)

# upass = getpass.getpass('输入密码： ')




# while True:
#     ra = random.randint(1, 10)
#     while True:
#         in_put = input('input number: ')
#         if not in_put.isdigit():
#             print('不是数字')
#             continue
#         try:
#             num = int(in_put)
#         except (ValueError, NameError):
#             print('输入错误！')
#             continue
#         except KeyboardInterrupt:
#             print('Bye-bye')
#             break
#         if num > ra:
#             print('大了')
#         elif num < ra:
#             print('小了')
#         else:
#             print('你猜对了！')
#             break
#     re = input('要继续吗：(y/n)')
#     if re in 'nN':
#         break

# while True:
#     score = input('input score: ')
#     if not score.isdigit():
#         print('输入错误！')
#         continue
#     num = int(score)
#     if num > 90:
#         print('你很优秀！')
#     elif num > 80:
#         print('良好！')
#     elif num > 70:
#         print('成就一般！')
#     elif num >= 60:
#         print('及格！')
#     else:
#         print('还需努力啊！')
#     answer = input('是否继续(y/n):')
#     if answer in 'Nn':
#         break


