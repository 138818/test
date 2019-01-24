import os
import pickle
import time

def update_info(fname, type):
    amoney = int(input('金额: '))
    day_time = time.strftime('%Y-%m-%d')
    coment = input('备注: ')
    with open(fname, 'rb') as fobj:
        all_data = pickle.load(fobj)

    if type == 'save':
        balance = all_data[-1][-2] + amoney
        result = (day_time, 0, amoney, balance, coment)
    else:
        balance = all_data[-1][-2] - amoney
        result = (day_time, amoney, 0, balance, coment)

    all_data.append(result)
    with open(fname, 'wb') as fobj:
        pickle.dump(all_data, fobj)

def save(fname):
    update_info(fname, 'save')

def cost(fname):
    update_info(fname, 'cost')

def query(fname):
    with open(fname, 'rb') as fobj:
        show_data = pickle.load(fobj)
        print('%s%s%s%s%s' % ('时间'.center(14), '支出'.center(12), '收入'.center(12), '余额'.center(12), '备注'.center(20)))
        for item in show_data:
            print('%s%s%s%s%s' % (item[0], item[1], item[2], item[3], item[4]))

def show_menu():
    prompt = """0) save
1) cost
2) query
3) quit
plese your choice: """
    cmds = {'0': save, '1': cost, '2': query}

    fname = 'account.data'
    if not os.path.exists(fname):
        init = [(time.strftime('%Y-%m-%d'), 0, 0, 10000, 'init')]
        with open(fname, 'wb') as fobj:
            pickle.dump(init, fobj)

    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('Invalid input')
        if choice == '3':
            break
        cmds[choice](fname)
if __name__ == '__main__':
    show_menu()