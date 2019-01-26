from urllib import request

header = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'} #定义访问头信息
r = request.Request('http://127.0.0.1', headers=header)
html = request.urlopen(r)
print(html.read())
