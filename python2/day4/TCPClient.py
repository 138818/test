import socket

host = '192.168.1.254'
port = 5555
addr = (host, port)
c = socket.socket()
c.connect(addr)

while True:
    data = input('> ') + '\r\n'
    c.send(data.encode())
    if data.strip() == 'quit':
        break
    reve_data = c.recv(4096)
    print('\r' + reve_data.decode(), end='')

c.close()

