class Vender:
    def __init__(self, company, tel):
        self.name = company
        self.tel = tel

    def call(self):
        print('Calling %s ....' % self.tel)

class wan_ju:
    def __init__(self, name, age, company, tel):
        self.name = name
        self.age = age
        self.vender = Vender(company, tel)

    def show_me(self):
        print('Hi,my name is %s, i\'m old is %s' % (self.name, self.age))


class New_wan_ju(wan_ju):
    def __init__(self,name, age, company, tel, size):
        super(New_wan_ju, self).__init__(name, age, company, tel)
        self.size = size

    def walk(self):
        print('walking.....')


wjy = New_wan_ju('wjy', 29, 'wjy.com', '13881833945', 'middle')
wjy.show_me()
