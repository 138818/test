from urllib import request
import re
import os
import urllib.error


def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)


def get_url(fname, patt, encoding=None):
    url_list = []
    cpatt = re.compile(patt)
    with open(fname, encoding=encoding) as fobj:
        for line in fobj:
            for m in cpatt.finditer(line):
                url_list.append(m.group())
    return url_list


def list_url(data):
    count = 0
    for item in data:
        count += 1
        print(item)
    print('共计: %s条' % count)

if __name__ == '__main__':
    fname = '/tmp/163.html'
    patt = '(http|https)://[-\w./_]+\.(png|jpg|jpeg|gif)'
    url = 'http://www.163.com/'
    # download(url, fname)
    url_list = get_url(fname, patt, encoding='gbk')
    # list_url(url_list)
    savedir = '/tmp/wangyi/'
    if not os.path.exists(savedir):
        os.mkdir(savedir)
    for url in url_list:

        fname = url.split('/')[-1]
        fname = os.path.join(savedir, fname)
        try:
            download(url, fname)
        except urllib.error.HTTPError:
            print(url)
