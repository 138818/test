import os
import tarfile

# tar = tarfile.open('/tmp/security.tar.gz', 'w:gz')
# tar.add('/etc/hosts')
# os.chdir('/etc')
# tar.add('security')
# tar.close()


# os.mkdir('/tmp/security')
os.chdir('/tmp/security')
tar = tarfile.open('/tmp/security.tar.gz', 'r:gz')
tar.extractall()
tar.close()