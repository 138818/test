import requests
import json

html = requests.get('http://www.baidu.com')
with open('/tmp/baidu.html', 'w') as fobj:
    fobj.write(html.text)


img = requests.get('http://img2.imgtn.bdimg.com/it/u=3240321934,1719795872&fm=26&gp=0.jpg')
with open('/tmp/my.jpg', 'wb') as fobj:
    fobj.write(img.content)


weater = requests.get('http://www.weather.com.cn/data/cityinfo/101270101.html')


# print(weater.encoding)
# print(weater.text)

weater.encoding = 'utf8'
# print(weater.encoding)
weater = json.loads(weater.text)['weatherinfo']
if __name__ == '__main__':

    print(weater)


# header = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
# r = requests.get('http://localhost', headers=header)
# print(r.status_code)   # 状态
# r = requests.get('http://localhost/abc', headers=header)
# print(r.status_code)
# print(r.raise_for_status)  #获取异常信息
