import requests
import pywasm
import json
import time
import math
import random

timestamp = int(time.time()) * 1000
t1 = int(timestamp / 1000 / 2)
t2 = int(timestamp / 1000 / 2 - math.floor(random.random() * 50  + 1))
vm = pywasm.load('./main.wasm')
result = vm.exec('encode', [t1, t2])
m_str = f'{result}|{t1}|{t2}'

header = {
    'user-agent': 'yuanrenxue.project'
}

cookie = {
    'sessionid': 'slxtnmw7bctear6zk9bxeafswatd5wpi'
}
url = 'https://match.yuanrenxue.cn/api/match/15'

ant = 0
for i in range(1, 6):
    page_num = str(i)
    param = {
        'm': m_str,
        'page': page_num
    }

    response = requests.get(url=url, params=param, cookies=cookie, headers=header).text
    json_data = json.loads(response)
    ant += sum(j['value'] for j in json_data['data'])
print(ant)