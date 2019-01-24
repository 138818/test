import getpass

name = input("请输入用户名: ")
password = getpass.getpass("password: ")
if (name == 'bob') and (password == '123456'):
    print("login successful!")
else:
    print("login inorrect")


