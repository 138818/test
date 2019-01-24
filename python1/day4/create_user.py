import sys
import subprocess
import randpass

def adduser(uname, upass, ufile):
    info = '''username: %s
userpassword: %s
''' % (uname, upass)
    subprocess.call('useradd %s' % uname, shell=True)
    subprocess.call('echo %s | passwd --stdin %s' % (upass, uname), shell=True)
    with open(ufile, 'a') as fobj:
        fobj.writelines(info)

if __name__ == '__main__':
    userpass = randpass.ran_pass()
    adduser(sys.argv[1], userpass, '/tmp/user.info')



