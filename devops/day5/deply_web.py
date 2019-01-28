import wget
import os
import requests
import hashlib
import tarfile


def has_new_version(live_url, live_fname):
    if not os.path.isfile(live_fname):
        return True

    with open(live_fname) as fobj:
        local_version = fobj.read()

    r = requests.get(live_url)
    if r.text != local_version:
        return True

    return False


def md5sum(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                return
            m.update(data)
    return m.hexdigest()


def deploy(app_fname, deploy_dir):
    os.chdir(deploy_dir)
    tar = tarfile.open(app_fname, 'r:gz')
    tar.extractall()
    tar.close()

    app_path = os.path.basename(app_fname)
    app_path = app_path.replace('.tar.gz', '')
    app_path = os.path.join(deploy_dir, app_path)
    dest_path = '/var/www/html/nsd1808'
    if os.path.exists(dest_path):
        os.unlink(dest_path)
    os.symlink(app_path, dest_path)


if __name__ == '__main__':
    live_url = 'http://192.168.1.55/deploy/live_version'
    live_fname = '/var/www/deploy/live_version'
    if not has_new_version(live_url, live_fname):
        print('没有新版本')
        exit()
    r = requests.get(live_url)
    download_dir = '/var/www/download'
    deploy_dir = '/var/www/deploy'
    app_url = 'http://192.168.1.55/deploy/packages/mysite_%s.tar.gz' % (r.text.strip())
    wget.download(app_url, download_dir)
    app_md5_url = app_url + '.md5'
    print(app_md5_url)
    wget.download(app_md5_url, download_dir)

    if os.path.exists(live_fname):
        os.remove(live_fname)
    wget.download(live_url, deploy_dir)
    app_fname = os.path.join(download_dir, app_url.split('/')[-1])
    local_md5 = md5sum(app_fname)
    r = requests.get(app_md5_url)
    if local_md5 != r.text.strip():
        print('校验失败')
        exit(1)

    deploy(app_fname, deploy_dir)
