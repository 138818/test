#!/usr/bin/env python3

import requests
import json

url = 'https://oapi.dingtalk.com/robot/send?access_token=9249d4a7193602a445fbe07df4d7e014c82f24a85e734fb16ee4d784ccf84f8a'
header = {'Content-Type': 'application/json;charset=utf-8'}
# 文本类
data1 = {
    'msgtype': 'text',
    'at': {
        'atMobiles': [13881833974,],
        'isAtAll': False,
    },
    'text': {
        'content': ''
    }
}

r = requests.post(url, data=json.dumps(data1), headers=header)