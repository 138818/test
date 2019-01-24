import random
def show(number, array):
    for i in range(1, number):
        if i in array:
            print(i, '出现的次数', array[i])
def balls(num = 5):
    chance = []
    while len(chance) < int(num):
        red = []
        blue = [random.randint(1, 16)]
        while len(red) < 6:
            temp = random.randint(1, 33)
            red.append(temp)
            red = list(set(red))
        t = []
        t.append(red)
        t.append(blue)
        chance.append(t)
    redTemp = {}
    blueTemp = {}
    for aa in chance:
        for bb in aa:
            for cc in bb:
                if len(bb) > 1:
                    if cc in redTemp:
                        redTemp[cc] = int(redTemp[cc]) + 1
                    else:
                        redTemp[cc] = 1
                else:
                    if cc in blueTemp:
                        blueTemp[cc] = int(blueTemp[cc]) + 1
                    else:
                        blueTemp[cc] = 1
    print('red list: ', len(redTemp))
    show(32, redTemp)
    print('blue list:', len(blueTemp))
    show(16, blueTemp)

c = input('input number: ')
balls(c)
