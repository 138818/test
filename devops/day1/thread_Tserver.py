import socket
import threading
from time import strftime


class ThreadTcpServer:
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
        cli_sock.close()

    def mainloop(self):
        while True:
            try:
                cli_sock, cli_address = self.s_sock.accept()
            except KeyboardInterrupt:
                break
            t = threading.Thread(target=self.chat(cli_sock))
            t.start()

        self.s_sock.close()


if __name__ == '__main__':

    tts = ThreadTcpServer('', 1234)
    tts.mainloop()
