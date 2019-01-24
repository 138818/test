
stack = []
def push_it():
    item = input('item to push > ').split()
    if item:
        stack.append(item)

def pop_it():
    if stack:
        print('from stack pop %s!' % stack.pop())

def view_it():
    print(stack)

def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    info = """(0)push it
(1)pop it
(2)view it
(3)quit
Please input your choice(0/1/2/3): """
    while True:
        input_info = input(info).split()[0]
        if input_info not in '0123':
            print('Invalid input, Try again.')
            continue
        if input_info == '3':
            print('Bye-bye')
            break

        cmds[input_info]()
        # if input_info == '0':
        #     push_it()
        # elif input_info == '1':
        #     pop_it()
        # else:
        #     view_it()


if __name__ == '__main__':
    show_menu()

