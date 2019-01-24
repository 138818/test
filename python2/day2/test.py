import random

# def func(*args):
#     print(args)
#
# def func2(**kwargs):
#     print(kwargs)
#
# def add(x, y):
#     print(x+y)
#
# if __name__ == '__main__':
#     func()
#     func('bob')
#     func('tom',123)
#     print('*' * 5)
#     func2()
#     func2(name = 'lucy', age = 123)
#     add(10, 20)
#     nums = (10, 20)
#     str = '11'
#     add(*str)
#
# def func(x):
#     return x % 2
#
# def func2(x):
#     return x * 2 + 1
#
# if __name__ == '__main__':
#     nums = [random.randint(1, 100) for i in range(10)]
#     print(nums)
#     print(list(filter(func, nums)))
#     print(list(filter(lambda x: x % 2, nums)))
#     print(list(map(func2, nums)))
#     print(list(map(lambda x: x * 2 + 1, nums)))
x = 100
# def func3():
#     x = '4'
#     print(x)
#
# func3()
# print(x)

# from functools import partial
#
# def func4(a,b,c,d):
#     print(a + b + c + d)
#
# func4(10, 20, 30, 5)
# myadd = partial(func4, 10, 20, 30)
# myadd(90)
#
#
# def func1(num):
#     if num == 1:
#         return 1
#     return num * func1(num-1)
# for i in range(1, 100):
#     print(func1(i))

# #
# def qsort(seq):
#     if len(seq) < 2:
#         return seq
#     middle = seq[0]
#     smaller = []
#     larger = []
#     for item in seq[1:]:
#         if item <= middle:
#             smaller.append(item)
#         else:
#             larger.append(item)
#
#     print(qsort(middle) + [middle] + qsort(larger))
#
# if __name__ == '__main__':
#     nums = [random.randint(1, 100) for i in range(10)]
#     print(nums)
#     qsort(nums)

# nums = [random.randint(1, 10) for i in range(3)]
# x = 0
# for a in range(len(nums)-1):
#     print('第一层 第%s次:' % x, nums)
#     y = 0
#     for b in range(len(nums) - x - 1):
#
#         print('第二层 第%s次: ' % y, nums)
#         if nums[y] > nums[y-1]:
#             temp = nums[y]
#             nums[y-1] = nums[y]
#             nums[y] = temp
#         y += 1
#
#     x += 1
# print(nums)
#
# def mygen():
#     yield 10
#     a = 100 + 200
#     yield a
#     yield 'hello'
#     yield [1,2,3,4]

# a = mygen()
# for i in a:
#     print(i)
