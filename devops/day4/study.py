from urllib import request
import json
# 101270101 成都

# 城市信息
cityinfo = request.urlopen('http://www.weather.com.cn/data/cityinfo/101270101.html')
# 实时情况
realTime = request.urlopen('http://www.weather.com.cn/data/sk/101270101.html')
# 天气指数
indexMark = request.urlopen('http://www.weather.com.cn/data/zs/101270101.html')

weatherInfo = [cityinfo, realTime, indexMark]
results = []
for data in weatherInfo:
    result = json.loads(data.read().decode())
    results.append(result)

for obj in results:
    for key in obj:
        for k in obj[key]:
            print('%s: %s ' % (k, obj[key][k]), end='')
        print('')
        print('*' * 10)

# http://m.weather.com.cn/img/n1.gif
