import random
import string

all_chs = string.digits+string.ascii_letters
def ran_pass(n=8):
    result = ''
    for ch in range(n):
        result += random.choice(all_chs)
    return result

if __name__ == '__main__':
    print(ran_pass(8))