import getpass
import pickle
import os
import subprocess


class Shopping:
    def __init__(self, file_goods, file_vip, file_user):
        self.file_goods = file_goods
        self.file_vip = file_vip
        self.file_user = file_user

        self.login_user = []

        self.goods_list = []
        self.user_list = [{'admin': 'admin'}]
        self.vip_list = []

    # *****************************************#
    # ************数据写入文件**********************#
    # ******************************************#

    def save_data(self, file, data):
        with open(file, 'wb') as fobj:
            for item in data:
                pickle.dump(item, fobj)

    # *****************************************#
    # ************提示信息**********************#
    # ******************************************#

    def show_menu(self, type):
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

    # *********************************************##
    # **************商品管理系统***********************#
    # **********************************************#

    def add_goods(self):
        while True:
            name = input('品名(输入end退出): ')
            if name == 'end':
                break
            price = input('单价: ')
            number = input('数量: ')
            states = 1
            new_data = {'code': '1', 'name': name, 'price': float(price), 'number': int(number), 'states': states}
            c = 0
            n = 1
            for data in self.goods_list:
                c += 1
                if data['name'] == name:
                    data['price'] = price
                    data['number'] = number
                    n = 0
                    break
            if n:
                new_data['code'] = str(c)
                self.goods_list.append(new_data)
        print('商品数据更新成功!')
        self.save_data(self.file_goods, self.goods_list)

    def update_goods(self):
        name = input('修改商品: ')
        n = 0
        for data in self.goods_list:
            if data['name'] == name:
                print(data)
                price = input('调整后单价: ')
                number = input('调整后数量: ')
                data['price'] = price
                data['number'] = number
                n = 1
                break
        if n:
            print('修改成功!')

        else:
            print('没有此商品!')
        self.save_data(self.file_goods, self.goods_list)

    def query_goods(self):
        print('品名\t价格($)\t库存')
        for data in self.goods_list:
            print('%s\t%s\t%s' % (data['name'], data['price'], data['number']))

    def sys_goods(self):
        goods_cmds = {'0': self.add_goods, '1': self.update_goods, '2': self.query_goods}
        while True:
            try:
                choice = input(self.show_menu('goods')).strip()[0]
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

    def show_goods_info(self):
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

    def print_info(self, array):
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
        self.save_data(self.file_goods, self.goods_list)
        input('')

    def sys_pay(self):
        che = []

        while True:
            codes = self.show_goods_info()
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
            self.print_info(che)

    # **********************************************#
    # ****************会员系统************************#
    # **********************************************#

    def add_vip(self):
        hname = input('会员姓名: ')
        htel = input('电话: ')
        n = 1
        for data in self.vip_list:
            if data['tel'] == htel:
                n = 0
                break

        if n:
            data = {'name': hname, 'tel': htel}
            self.vip_list.append(data)
            print('新增会员:\n', data)
        else:
            print('电话为%s的会员已存在!')
        self.save_data(self.file_vip, self.vip_list)

    def update_vip(self):
        htel = input('旧电话: ')
        n = 1
        for data in self.vip_list:
            if data['tel'] == htel:
                newhtel = input('新号码: ')
                data['tel'] = newhtel
                print('操作成功!')
                n = 0
                break

        if n: print('没有此会员')
        self.save_data(self.file_vip, self.vip_list)

    def query_vip(self):
        print('*' * 30)
        print('%-8s%-8s' % ('姓名', '电话'))
        for data in self.vip_list:
            print('%-8s%-8s' % (data['name'], data['tel']))

        print("*" * 30)

    def sys_vip(self):
        vip_cmds = {'0': self.add_vip, '1': self.update_vip, '2': self.query_vip}
        while True:
            choice = input(self.show_menu('vip')).strip()[0]
            if choice not in '0123':
                print('Invalid input')
            if choice == '3':
                break
            vip_cmds[choice]()

    # *************初始化数读取数据***************#

    def check_file(self):
        if not os.path.exists(self.file_goods):
            subprocess.call('touch %s' % self.file_goods, shell=True)
        if not os.path.exists(self.file_vip):
            subprocess.call('touch %s' % self.file_vip, shell=True)
        if not os.path.exists(self.file_user):
            with open(self.file_user, 'wb') as fobj:
                data = {"admin": 'admin'}
                pickle.dump(data, fobj)

    def init_data(self, file, data_list):
        with open(file, 'rb') as fobj:
            while True:
                try:
                    data = pickle.load(fobj)
                except EOFError:
                    break
                data_list.append(data)

    # *****************登陆验证******************#

    def check_login(self, loginName, loginPass):
        n = 0
        for item in self.user_list:
            if item.get(loginName, 0) and item[loginName] == loginPass:
                n = 1
                break

        return n

    # *****************菜单入口*****************#

    def _main(self):
        self.check_file()
        self.init_data(self.file_goods, self.goods_list)
        self.init_data(self.file_vip, self.vip_list)
        self.init_data(self.file_user, self.user_list)

        uname = input('用户名: ')
        upass = getpass.getpass('密码: ')

        if self.check_login(uname, upass):
            self.login_user.append(uname)
            main_cmds = {'0': self.sys_pay, '1': self.sys_vip, '2': self.sys_goods}
            while True:
                choice = input(self.show_menu('main')).strip()[0]
                if choice not in '0123':
                    print('Invalid input')
                if choice == '3':
                    break
                main_cmds[choice]()


if __name__ == '__main__':
    goods_info = '/root/shopping/goods.data'
    vip_info = '/root/shopping/vip.data'
    user_info = '/root/shopping/user.data'
    shopping = Shopping(goods_info, vip_info, user_info)
    shopping._main()
