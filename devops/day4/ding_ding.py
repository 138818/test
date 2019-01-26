import requests
import json
import sys
import my_requests as tianqi


def jqr(url):
    header = {'Content-Type': 'application/json;charset=utf-8'}
    # 文本类
    data1 = {
        'msgtype': 'text',
        'at': {
            'atMobiles': receivers,
            'isAtAll': True,
        },
        'text': {
            'content': content
        }
    }
    # 连接类
    # data2 = {
    #     'msgtype': 'link',
    #     'link': {
    #         'text': content,
    #         'title': 'bbbbbbbbbbbbbbbbbb',
    #         'picUrl': '',
    #         'messageUrl': 'http://img4.imgtn.bdimg.com/it/u=2827954235,571429697&fm=26&gp=0.jpg'
    #     }
    # }


    # data3 = {
    #     'msgtype': 'markdown',
    #     'markdown': {"title":"杭州天气",
    #         "text":"#### 杭州天气  \n > 9度，@1825718XXXX 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](https://www.seniverse.com/) "},
    #     'at': {
    #         'atMobiles':  [],
    #         'isAtAll': True,
    #     }
    # }

    r = requests.post(url, data=json.dumps(data1), headers=header)
    return r.text



if __name__ == '__main__':
    url = 'https://oapi.dingtalk.com/robot/send?access_token=9249d4a7193602a445fbe07df4d7e014c82f24a85e734fb16ee4d784ccf84f8a'
    # recerives = []
    # content = sys.argv[1]
    # content = 'nice nice'
    print(jqr(url))
# http://img4.imgtn.bdimg.com/it/u=2827954235,571429697&fm=26&gp=0.jpg

# down.51cto.com  #电子书下载