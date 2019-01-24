import os
from time import strftime
import socket

class ForkTServer:
    def __init__(self, host, port):
        self.address = (host, port)
        self.s_sock = socket.socket()
        self.s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s_sock.bind(self.address)
        self.s_sock.listen(1)


    def chat(self, cli_sock):
        while True:
            data = cli_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode())
            cli_sock.send(data.encode())

    def _server(self):
        while True:
            try:
                cli_sock, cli_address = self.s_sock.accept()
            except KeyboardInterrupt:
                break
            ret_val = os.fork()
            if not ret_val:
                self.s_sock.close()
                self.chat(cli_sock)
                cli_sock.close()
                exit()
            cli_sock.close()

            while True:
                kill_zombie = os.waitpid(-1, 1)
                if kill_zombie[0] == 0:
                    break
        self.s_sock.close()

if __name__ == '__main__':
    obj = ForkTServer('', 1234)
    obj._server()



