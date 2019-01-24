import random

def rpass(length = 8):
    ch = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-+/*&^%$#@!~'
    my_pass = ""
    while len(my_pass) < int(length):
        my_pass += str(random.choice(ch))
    return my_pass

num = input('Please enter your password number: ')
if num == None:
    print(rpass())
else:
    print(rpass(num))


