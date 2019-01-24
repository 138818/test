import time

def railway(length, speek):
    print('#' * length, end='')
    n = 0
    while True:
        time.sleep(speek)
        print('\r%s>%s' % ('#' * n, '#' * (length-1 - n)), end='')
        n += 1
        if n == length:
           n = 0

if __name__ == '__main__':
    railway(30, 0.5)


