import paramiko
import threading
import sys
import getpass


# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('192.168.1.100', username='root', password='1')
# resutl = ssh.exec_command('mkdir /tmp/demo')
#
# ssh.close()
#
#
def ssh_host(host, user='root', password='1', command='ls'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:
        print(out.decode())
    if err:
        print(err.decode())
    ssh.close()


if __name__ == '__main__':
    files = sys.argv[1]
    cmd = sys.argv[2]
    password = getpass.getpass('pass: ')
    with open(files) as fobj:
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=ssh_host, args=(ip, 'root', password, cmd))
            t.start()

            # ssh_host(ip, password=password, command=cmd)

