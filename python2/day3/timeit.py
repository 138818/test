import time

def deco1(func):
    def changeColor():
        print("\033[31m%s\033[0m" % func())
    return changeColor


def deco(func):
    def timeit():
        star = time.time()
        func()
        end = time.time()
        print(end - star)
    return timeit

@deco
def myadd():
    resutl = 0
    for i in range(100000000):
        resutl += i
    print(resutl)

@deco1
def pri():
   return 'ni hao '


if __name__ == '__main__':
    pri()