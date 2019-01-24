import getpass
import hashlib
from db_base import Session, User, Goods, VipUser

session = Session()

# *****************************************#
# ************提示信息**********************#
# ******************************************#

def show_menu(type):
    main_menu = """
********欢迎使用wjy系统**********
0) 销售系统\n1) 会员系统\n2) 商品系统\n3) 退出\n请选择: """

    vip_menu = """
************会员系统************
0) 新增\n1) 修改\n2) 查询\n3) 返回\n请选择: """

    goods_menu = """
************商品系统************
0) 新增\n1) 修改\n2) 查询\n3) 返回\n请选择: """
    all_info = {'main': main_menu, 'goods': goods_menu, 'vip': vip_menu}

    return all_info[type]


def show_goods_info():
    c = 1
    nums = []
    for item in self.goods_list:
        if item['states']:
            nums.append(item['code'])
            if c % 5 == 0:
                print('(%s)%s ' % (item['code'], item['name']))
            else:
                print('(%s)%s ' % (item['code'], item['name']), end='')
            c += 1
    return nums


# *********************************************##
# **************商品管理系统***********************#
# **********************************************#

def add_goods():

    while True:
        name = input('品名(输入end退出): ')
        if name == 'end':
            break
        price = input('单价: ')
        number = input('数量: ')

        goods = Goods(g_name=name, g_price=price, g_number=number, states=1)
        session.add(goods)
        session.commit()
    print('商品数据更新成功!')


def update_goods():
    show_goods_info()
    code = input('商品编码: ')
    price = input('调整后单价: ')
    number = input('调整后数量: ')
    states = input('1.上架 0.下架: ')
    goods = session.query(Goods).filter(Goods.g_id==int(code))
    goods = goods.one()
    goods.g_price = price
    goods.g_number = number
    goods.states = states
    session.commit()
    print('商品更新成功!')


def query_goods():
    goods = session.query(Goods).all()
    print('品名\t\t价格($)\t\t库存\t\t状态')
    for data in goods:
        print('%-8s%-8s\t%-5s\t%-5s' % (data.g_name, data.g_price, data.g_number, data.states))


def sys_goods():
    goods_cmds = {'0': add_goods, '1': update_goods, '2': query_goods}
    while True:
        try:
            choice = input(show_menu('goods')).strip()[0]
        except IndexError:
            break
        if choice not in '0123':
            print('Invalid input')
        if choice == '3':
            break
        goods_cmds[choice]()

# *********************************************#
# *****************销售系统**********************#
# *********************************************#


def print_info(array):
    codelist = []
    for item in array:
        for sp in self.goods_list:
            if sp['code'] == item[0]:
                sp['number'] = sp['number'] - item[1]
                codelist.append([sp['name'], item[1], float(item[1]) * float(sp['price'])])
                continue

    print('*********商品详情**********')
    sumMoney = 0
    count = 0
    for goods in codelist:
        print("""%s\t%s\t%s""" % (goods[0], goods[1], goods[2]))
        sumMoney += goods[2]
        count += int(goods[1])
    print('***************************')
    print('合计: %s\t数量: %s' % (sumMoney, count))
    money = input('实收金额: ')
    give = float(money) - float(sumMoney)
    print('实收金额: %s\t找零: %s' % (money, give))
    # save_data(file_goods, goods_list)
    input('')

def sys_pay():
    che = []

    while True:
        codes = show_goods_info()
        code = input('\n选择编码(输入end结束):')
        if code == 'end':
            break
        if code not in codes:
            print('无效商品!')
            continue
        num = input('购买数量: ')
        che.append([code, int(num)])

    print('')
    if len(che):
        print_info(che)

# **********************************************#
# ****************会员系统************************#
# **********************************************#

def add_vip():
    hname = input('会员姓名: ')
    htel = input('电话: ')
    birthday = input('生日: ')
    vip = VipUser(v_name=hname, telphone=htel, birthday=birthday)
    session.add(vip)
    session.commit()



def update_vip():
    oldtel = input('旧电话: ')
    newtel = input('新电话')
    birthday = input('生日: ')
    vipuser = session.query(VipUser).filter(VipUser.telphone==oldtel)
    vipuser = vipuser.one()
    vipuser.telphone = newtel
    vipuser.birthday = birthday
    session.commit()


def query_vip():
    vipusers = session.query(VipUser).all()
    print('*' * 30)
    print('%-8s%-15s%-8s' % ('姓名', '电话', '生日'))
    for data in vipusers:
        print('%-8s%-15s%-8s' % (data.v_name, data.telphone, data.birthday))
    print("*" * 30)

def sys_vip():
    vip_cmds = {'0': add_vip, '1': update_vip, '2': query_vip}
    while True:
        choice = input(show_menu('vip')).strip()[0]
        if choice not in '0123':
            print('Invalid input')
        if choice == '3':
            break
        vip_cmds[choice]()


# *****************菜单入口*****************#
def _main():
    uname = input('用户名: ')
    upass = getpass.getpass('密码: ')
    upass = hashlib.md5(upass.encode('utf-8'))
    upass = upass.hexdigest()
    result = session.query(User).filter(User.name==uname).filter(User.password==upass)
    result = result.scalar()
    if result:
        main_cmds = {'0': sys_pay, '1': sys_vip, '2': sys_goods}
        while True:
            choice = input(show_menu('main')).strip()[0]
            if choice not in '0123':
                print('Invalid input')
            if choice == '3':
                break
            main_cmds[choice]()

if __name__ == '__main__':
    _main()