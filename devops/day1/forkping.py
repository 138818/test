import os
import subprocess

def myping(host):
    result = subprocess.call('ping -c2 %s &>/dev/null' % host, shell=True)
    if result == 0:
        print('%s is up' % host)
    else:
        print('%s is down' % host)

if __name__ == '__main__':
    ips = ('176.204.26.%s' % i for i in range(1, 254))
    for ip in ips:
        fock_s = os.fork()
        if not fock_s:
            myping(ip)
            exit()