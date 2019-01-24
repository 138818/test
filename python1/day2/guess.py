import random
number = random.randint(1, 10)
count = 0
while count < 3:
    answer = int(input('number: '))
    if number > answer:
        print('小了!')
    elif number < answer:
        print('大了!')
    else:
        print('yes,guess right!')
        break
    count += 1
else:
    print('result:', number)
############################################
# a, b = 30, 20
# small = a if a <= b else b
# print(small)

# chance = []
# answer = int(input("input number: "))
# while 0 != answer:
#     RedNumber = []
#     BlueNumber = random.randint(1, 16)
#     while len(RedNumber) < 6:
#         temp = random.randint(1, 33)
#         RedNumber.append(temp)
#         RedNumber = list(set(RedNumber))
#     red = ""
#     RedNumber.sort()
#     for c in RedNumber:
#         red = red+str(c)+" "
#     result = '\033[31;1m%s\033[0m\033[34;1m%s\033[0m' % (red, BlueNumber)
#     print(result)
#     answer -= 1
######################################################
