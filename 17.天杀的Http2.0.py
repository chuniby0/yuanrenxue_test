import httpx
import json

url = 'https://match.yuanrenxue.cn/api/match/17'
header = {
    'user-agent': 'yuanrenxue.project'
}
cookie = {
    'sessionid': 'g3a8d57de325zsak72gt6ii6wi0a9l22',
    'referer': 'https://match.yuanrenxue.cn/match/17',
    'yuanrenxue_cookie': '1681872736|ASMjrcwoWWgKqNx9jSwcuQa6mu1LnZyxJlH1QJ0dE2rlDi6GzoiAYLbVJQQTKJDz2ZsjFg1MMXIlvB3nGPa08mqrIAqZYFukJQ7CSNgnbO3Jztd5gaOjvxB'
}
ant = 0
for i in range(1, 6):
    page_num = str(i)
    param = {
        'page': page_num
    }
    client = httpx.Client(http2=True)
    response = client.get(url=url, headers=header, cookies=cookie, params=param).text
    json_data = json.loads(response)
    ant += sum(j['value'] for j in json_data['data'])
print(ant)