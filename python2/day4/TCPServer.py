import socket

host = ''
port = 1234
addr = (host, port)
s = socket.socket()  #默认创建TCP套节字
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #服务停止后能能马上启动
s.bind(addr)  #绑定套节字
s.listen(1)   #监听端口
while True:
    try:
        cli_sock, cli_addr = s.accept()
    except KeyboardInterrupt:
        break
    print(str(cli_addr))
    while True:
        data = cli_sock.recv(4096)  #接收的数据是bytes类型
        if data.strip() == b'quit':
            break
        print(data.decode(), end='')  #把bytes转为str输出
        send_data = input('>')
        cli_sock.send(b'%s\r\n' % send_data.encode())  #把str转发bytes发送
    cli_sock.close()

s.close()

