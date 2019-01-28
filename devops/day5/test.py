import os
import requests
import wget

live_url = 'http://192.168.1.55/deploy/live_version'
live_fname = '/var/www/deploy/live_version'

def has_new_version(live_url, live_fname):
    if not os.path.isfile(live_fname):
        return True

    with open(live_fname) as fobj:
        local_version = fobj.read()

    r = requests.get(live_url)
    if r.text != local_version:
        return True

    return False



if __name__ == '__main__':
    # live_url = 'http://192.168.1.55/deploy/live_version'
    # live_fname = '/var/www/deploy/live_version'
    # if not has_new_version(live_url, live_fname):
    #     print('没有新版本')
    #     exit()
    # r = requests.get(live_url)
    download_dir = '/var/www/download'
    deploy_dir = '/var/www/deploy'
    # app_url = 'http://192.168.1.55/deploy/packages/mysite_%s.tar.gz' % (r.text.strip())
    # print(app_url)
    uu = 'http://img5.imgtn.bdimg.com/it/u=2230167403,4188800858&fm=26&gp=0.jpg'
    wget.download(uu, download_dir)
