import re
from urllib import request
import wget
import paramiko
import psutil
import libvirt


print(request.quote('小夜曲'))
#
# print(request.quote('hello'))
#
# url = 'https://www.sogou.com/web?query=%s'
# param = request.quote('中国')
# html = request.urlopen(url % param)
# with open('/tmp/china.html', 'wb') as fobj:
#     fobj.write(html.read())

#
# header = {'User-agent': 'test'}
# url = request.Request('http://127.0.0.1', headers=header)
# html = request.urlopen(url)
# data = html.read()
#
# print(data)

# for item in html.read():
#     print(item)

# wget.download('http://cdn.tmooc.cn/bsfile//imgad///247B30A693DC4477BB4B40A7D4B2196A.png')
wget.download('http://cdn.tmooc.cn/bsfile//imgad///247B30A693DC4477BB4B40A7D4B2196A.png', '/root/')
