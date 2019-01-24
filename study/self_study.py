import random
import getpass
import shutil
import os


def _01(info):
    print(info)


def _02():
    print('hello world')
    print('hello', 'world')
    print('hello' + 'world')
    print('hello', 'world', sep='**')
    print('hao are your', end='')


def _03():
    print(5 + 2)
    print(5 - 2)
    print(5 * 2)
    print(5 / 2)
    print(5 // 2)
    print(5 % 2)
    print(5 ** 2)
    print(20 > 10 > 5)
    print(20 > 10 and 10 > 5)
    print(not 20 > 10)


def _04():
    number = input('请输入数字: ')
    print(number)
    print(type(number))
    print(int(number) + 5)
    print(str(number) + 'string')


def _05():
    uname = input('输入你的名字: ')
    print('你的名字是: ', uname)
    print('你的名字是: ' + uname)


def _06():
    sentence = 'tom\'s pet is cat'
    sentence1 = "tom said:\"hello world\""
    sentence2 = "tom's pet is cat"
    sentence3 = 'tom said:"hello world"'
    words = '''
    hello
    world
    abcd'''
    py_str = "python"
    len(py_str)  # 取长度
    py_str[0]  # 第一个字符
    'python'[0]
    py_str[-1]  # 最后一个字符
    # py_str[6]  # 错误，下标超出范围
    py_str[2:4]  # 切片，起始下标包含，结束下标不包含
    py_str[2:]  # 从下标为2的字符取到结尾
    py_str[:2]  # 从开头取到下标是2之前的字符
    py_str[:]  # 取全部
    py_str[::2]  # 步长值为2，默认是1
    py_str[1::2]  # 取出yhn
    py_str[::-1]  # 步长为负，表示自右向左取

    py_str + 'is good'
    py_str * 3

    't' in py_str  # True
    'th' in py_str  # True
    'to' in py_str  # False
    'to' not in py_str  # True


def _07():
    alist = [10, 20, 30, 'bob', 'alice', [1, 2, 3]]
    len(alist)
    alist[-1]  # 取出最后一项
    alist[-1][-1]  # 因为最后一项是列表，列表还可以继续取下标
    [1, 2, 3][-1]  # [1,2,3]是列表，[-1]表示列表最后一项
    alist[-2][2]  # 列表倒数第2项是字符串，再取出字符下标为2的字符
    alist[3:5]  # ['bob', 'alice']
    10 in alist  # True
    'o' in alist  # False
    100 not in alist  # True
    alist[-1] = 100  # 修改最后一项的值


def _08():
    atuple = (10, 20, 30, 'bob', 'alice', [1, 2, 3])
    len(atuple)
    10 in atuple
    atuple[2]
    atuple[3:5]
    # atuple[-1] = 100  # 错误，元组是不可变的


def _09():
    # 字典是key-value(键－值）对形式的，没有顺序，通过键取出值
    adict = {'name': 'bob', 'age': 23}
    len(adict)
    'bob' in adict  # False
    'name' in adict  # True
    adict['email'] = 'bob@tedu.cn'  # 字典中没有key，则添加新项目
    adict['age'] = 25  # 字典中已有key，修改对应的value


def _10():
    if 3 > 0:
        print('yes')
        print('ok')

    if 10 in [10, 20, 30]:
        print('ok')

    if -0.0:
        print('yes')  # 任何值为0的数字都是False

    if [1, 2]:
        print('yes')  # 非空对象都是True

    if ' ':
        print('yes')  # 空格字符也是字符，条件为True


def _11():
    a = 10
    b = 20
    if a < b:
        smailler = a
    else:
        smailler = b

    s = a if a < b else b  # 和上面的if-else语句等价
    print(s)


def _12():
    uname = input('输入名字: ')
    upass = getpass.getpass('输入密码: ')
    if uname == 'tom' and upass == '123456':
        print('login successful')
    else:
        print('login fail!')


def guess_number():
    try:
        num = random.randint(1, 100)
        while True:
            youNum = int(input('input your number: '))
            if num > youNum:
                print("小了")
            elif num < youNum:
                print('大了')
            else:
                print('you are right')
                break
    except:
        print('input error!')
    finally:
        print('Bye-bye!')


def _14():
    sorce = int(input('your sorce: '))
    if sorce > 90:
        print('优秀')
    elif sorce > 80:
        print('良好')
    elif sorce > 70:
        print('一般')
    elif sorce > 60:
        print('及格')
    else:
        print('还得鲁里亚')


def guess_finger():
    all_choices = ['石头', '剪刀', '布']
    win_choices = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
    info = "\n请出拳(0.石头 1.剪刀 2.布 3.quit): "
    try:
        while True:
            computer = random.randint(0, 2)
            player = input(info).strip()[0]
            print('你的选择: %s  电脑选择: %s' % (all_choices[int(player)], all_choices[int(computer)]))
            if computer == player:
                print('\033[32;1m平局!\033[0m')
            elif [all_choices[int(player)], all_choices[computer]] in win_choices:
                print('\033[33;1m恭喜你,赢了!\033[0m')
            else:
                print('\033[34;1m你输了!\033[0m')
    except (TypeError, IndexError, ValueError):
        if player != '3':
            print('\033[31;1m输入错误!\033[0m')
    except KeyboardInterrupt:
        print('\nBye-bye!')
    finally:
        print('Bye-bye')

def _15():
    sum = 0
    for i in range(1, 101):
        sum += i
    print(sum)


def _16():
    alist = [0, 1]
    for i in range(8):
        alist.append(alist[-1] + alist[-2])
    print(alist)

def _17():
    alist = [a for a in range(10)]
    blist = [b for b in range(3, 10)]
    clist = [c for c in range(1, 100, 2)]
    dlist = [d for d in range(100, 1, -2)]
    print(alist)
    print(blist)
    print(clist)
    print(dlist)

def jiu_jiu(n=9):
    for a in range(1, n+1):
        for b in range(1, a+1):
            print('%s X %s = %-4s' % (a, b, a*b), end='')
        print('')

def create_ip():
    iplist = ['192.168.0.%s' % i for i in range(1, 255)]
    print(iplist)


def f_read1(fname):
    # fobj = open(fname, 'r')
    # data = fobj.read()
    # print(data)
    # fobj.close()
    with open(fname, 'r') as fobj:
        data = fobj.read()
        print(data)

def f_read2(fname):
    # fobj = open(fname, 'r')
    # while True:
    #     data = fobj.read(4096)
    #     if not data:
    #         break
    #     print(data)
    # fobj.close()
    # with open(fname, 'r') as fobj:
    #     while True:
    #         data = fobj.read(4096)
    #         if not data:
    #             break
    #         print(data)
    with open(fname, 'r') as fobj:
        while True:
            data = fobj.readline()
            if not data:
                break
            print(data)

def f_read3(fname):
    fobj = open(fname, 'r')
    for line in fobj:
        print(line)
    fobj.close()

def f_read4(fname):
    # fobj = open(fname, 'r')
    # data = fobj.readlines()
    # print(data[1])
    # fobj.close()

    with open(fname, 'r') as fobj:
        data = fobj.readlines(10)
        print(data)

def f_write1(fname):
    # fobj = open(fname, 'w')
    # fobj.write('ni hao \n')
    # fobj.flush()
    # fobj.close()
    with open(fname, 'w') as fobj:
        fobj.writelines('nice to meet your\n')

def f_write2(fname):
    with open(fname, 'w') as fobj:
        fobj.writelines(['1. 111111111\n', '2.2222222222222\n'])


if __name__ == '__main__':
    f_write2('/tmp/abc.txt')

