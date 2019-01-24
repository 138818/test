import random

# def add(x, y):
#     return x + y
#
# def sub(x, y):
#     return x - y

def exam():
    # cmds = {'+': add, '-': sub}
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [random.randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    ty = random.choice('+-')
    # result = cmds[ty](*nums)
    result = cmds[ty](*nums)
    count = 0

    while count < 3:
        try:
            answer = int(input('%s %s %s = ' % (nums[0], ty, nums[1])))
        except:
            print()
            continue
        if answer == result:
            print('Very Good!')
            break
        print('Wrong Answer!')
        count += 1
    else:
        print('%s %s %s = %s' % (nums[0], ty, nums[1], result))

def main():
    while True:
        exam()
        try:
            yn = input('是否继续(y/n): ')
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()

