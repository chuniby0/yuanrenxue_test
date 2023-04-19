import requests
import re
import json

url_cookie = 'https://match.yuanrenxue.com/match/13'
url_data = 'https://match.yuanrenxue.cn/api/match/13'
cookie = {
    'sessionid': 'g3a8d57de325zsak72gt6ii6wi0a9l22'
    }
header = {
    'User-Agent': 'yuanrenxue.project'
}

session = requests.Session()
session.cookies.update(cookie)
res = session.get(url=url_cookie).text

com = re.compile(".*?\('(.*?)'\).*?")
# "'([a-zA-Z0-9=_|])'"
cookie_ = com.findall(res)
key, value = ''.join(cookie_).split('=')
session.headers = header
session.cookies.update({key: value})

ant = 0
for i in range(1, 6):
    page_num = str(i)
    param = {
        'page': page_num
    }
    response = session.get(url=url_data, params=param).text
    json_data = json.loads(response)
    ant += sum(j['value'] for j in json_data['data'])
print(ant)