import socket
from time import strftime

class _server:
    def __init__(self, host='', port=1234):
        self.address = (host, port)
        self.s_obj = socket.socket()
        self.s_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s_obj.bind(self.address)
        self.s_obj.listen(1)

    def chat(self, client_sock):
        while True:
            data = client_sock.recv(1024)
            if data.strip() == b'quit':
                break
            # print(data, end='')
            data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode())
            client_sock.send(data.encode())

    def _start(self):
        while True:
            try:
                client_sock, client_address = self.s_obj.accept()
            except KeyboardInterrupt:
                break
            self.chat(client_sock)
            client_sock.close()
        self.s_obj.close()

if __name__ == '__main__':
    time_server = _server()
    time_server._start()

