
def plankRoad():
    mylist = []
    while True:
        choice = input("请选择:(1.压栈 2.出栈 3.查询)")
        if choice == '1':
            item = input('压栈内容> ')
            mylist.append(item)
        elif choice == '2':
            item = input('出栈内容> ')
            if item not in mylist:
                print('没有此项')
                continue
            ind = mylist.index(item)
            mylist.pop(ind)
        elif choice == '3':
            print(mylist, '\n')
        else:
            print('\n选择错误,程序已结束!')
            break

if __name__ == '__main__':
    plankRoad()

