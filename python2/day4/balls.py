import random
from collections import Counter


class MyBalls:
    def __init__(self, type):
        self.type = type

    # 随机产生红球
    def _red(self, number=1):
        for i in range(number):
            all_data = []
            while len(all_data) <= number:
                item = [random.randint(1, 33) for i in range(6)]
                item = list(set(item))
                if len(item) != 6:
                    continue
                all_data = all_data + item
        result = Counter(all_data).most_common(6)
        for n in result:
            print('\033[31;m%s \033[0m' % n[0], end='')

    # 随机产生绿球
    def _blue(self, number=1):
        for i in range(number):
            all_data = []
            while len(all_data) <= number:
                item = [random.randint(1, 16) for i in range(1)]
                all_data = all_data + item
        result = Counter(all_data).most_common(1)
        for n in result:
            print('\033[34;m%s\033[0m' % n[0])

    def _result(self, number=1):
        self._red(number)
        self._blue(number)


if __name__ == '__main__':
    ball = MyBalls('red')
    ball._result()