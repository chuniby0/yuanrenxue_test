import requests
import base64
import json

code_str = 'yuanrenxue'
url = 'https://match.yuanrenxue.cn/api/match/12'
ant = 0
header = {
    'user-agent': 'yuanrenxue.project',
    'cookie': 'sessionid=hw7b354zdfo9992d5p1pr2lppp8inqa5'
}
for i in range(1, 6):
    num = str(i)
    code_m = code_str + num
    code_m = base64.b64encode(code_m.encode('utf-8')).decode('utf-8')

    param = {
        'page': num,
        'm': code_m
    }

    res = requests.get(url=url, params=param, headers=header).text
    res = json.loads(res)

    ant += sum(j['value'] for j in res['data'])

print(ant)