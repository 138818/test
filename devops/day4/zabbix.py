import requests
import json

url = 'http://192.168.1.100/zabbix/api_jsonrpc.php'
header = {'Content-Type': 'application/json-rpc'}
# 查看版本
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1
# }

# data1 = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }

data2 = {
    'jsonrpc': '2.0',
    'method': 'user.get',
    'params': {
        'output': 'extend'
    },
    'auth': 'cec00a2f12545c3e31dfedb17861c1f5',
    'id': 1
}

# 获取所有的主机组信息
data3 = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        # "filter": {
        #     "name": [
        #         "Zabbix servers",
        #         "Linux servers"
        #     ]
        # }
    },
    "auth": "cec00a2f12545c3e31dfedb17861c1f5",
    "id": 1
}

# 获取模板信息
data4 = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": "extend",
        "filter": {
            "host": [
                "Template OS Linux",
            ]
        }
    },
    "auth": "cec00a2f12545c3e31dfedb17861c1f5",
    "id": 1
}

# 创建名为mysql的主机，它在Linux servers组中，应用Template OS Linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "Zabbix Server",
        "interfaces": [   # 接口，采用什么方式监控webserver1
            {
                "type": 1,   # 采用zabbix agent方式监控
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.2",   # webserver1的IP
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,   # 主机资产记录
        "inventory": {
            "macaddress_a": "01234a32254",
            "macaddress_b": "567682342zj"
        }
    },
    "auth": "ae10101387ba2ef5b224beb18fd5732a",
    "id": 1
}


# 'templateid': '10001'
r = requests.post(url, headers=header, data=json.dumps(data2))
print(r.json())
r = requests.post(url, headers=header, data=json.dumps(data3))
print(r.json())
r = requests.post(url, headers=header, data=json.dumps(data4))
print(r.json())
# 'userid': '1', 'alias': 'Admin', 'name': 'Zabbix',
# 'surname': 'Administrator', 'url': '', 'autologin': '1',
# 'autologout': '0', 'lang': 'zh_CN', 'refresh': '30s',
# 'type': '3', 'theme': 'default', 'attempt_failed': '0',
# 'attempt_ip': '', 'attempt_clock': '0', 'rows_per_page': '50'}

