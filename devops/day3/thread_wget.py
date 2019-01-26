import threading
import wget
import os
import re
from urllib import request


def down_data(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)


def url_list(fname, patt, encoding=None):
    urls = []
    cpatt = re.compile(patt)
    with open(fname) as fobj:
        for line in fobj:

            for m in cpatt.finditer(line):
                urls.append(m.group())
    return urls


def wget_data(url, dest):
    wget.download(url, dest)


if __name__ == '__main__':
    url = 'http://www.ifeng.com'
    fname = '/tmp/ifeng.html'
    patt = '(http|https)://[-\w./_]+\.(png|jpg|jpeg|gif)'
    encode = ''
    # down_data(url, fname)
    urls = url_list(fname, patt, None)
    print(len(urls))
    dest = '/tmp/ifeng/'
    if not os.path.exists(dest):
        os.mkdir(dest)
    for u in urls:
        print(u)
        t = threading.Thread(wget_data(u, dest))
        t.start()
