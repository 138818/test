import getpass
userdb = {}

def register():
    username = input('input your name: ').strip()
    if username in userdb:
        print('%s已存在' % username)
    else:
        userpass = getpass.getpass('input your passowrd: ').strip()
        userdb[username] = userpass

def login():
    uname = input('name: ').strip()
    upass = getpass.getpass('passowrd: ').strip()
    if userdb.get(uname) == upass:
        print('登陆成功!')
    else:
        print('登陆失败')

def show_menu():
    show_info = """(0)register\n(1)login\n(2)quit\n请选择:"""
    cmds = {'0': register, '1': login}
    while True:
        input_choice = input(show_info).strip()[0]
        if input_choice not in '012':
            print('Invalid input,Try again.')
            continue
        if input_choice == '2':
            break
        cmds[input_choice]()

if __name__ == '__main__':
    show_menu()


