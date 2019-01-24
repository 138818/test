import threading
import subprocess


# def ping(host):
#     result = subprocess.call('ping -c2 %s &> /dev/null' % host, shell=True)
#     if result == 0:
#         print('\033[33;m%s is up\033[0m' % host)
#     else:
#         print('\033[31;m%s is down\033[0m' % host)
#
#
# if __name__ == '__main__':
#     ips = ('176.204.26.%s' % i for i in range(1, 255))
#
#     for ip in ips:
#         t = threading.Thread(target=ping, args=(ip,))
#         t.start()


class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        result = subprocess.call('ping -c2 %s &> /dev/null' % self.host, shell=True)
        if result == 0:
            print('\033[33;m%s is up\033[0m' % self.host)
        else:
            print('\033[31;m%s is down\033[0m' % self.host)


if __name__ == '__main__':
    ips = ('176.204.26.%s' % i for i in range(1, 255))
    for ip in ips:
        t = threading.Thread(target=Ping(ip))
        t.start()
