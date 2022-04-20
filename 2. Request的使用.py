'''
@Author  : heyheyheyJoy
@Time    : 2022/3/13 8:20 下午
@File    : 2. Request的使用.py
'''

from urllib.request import urlopen
from urllib.request import Request

url = "http://www.baidu.com"

headers = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

request = Request(url, headers=headers)
print(request.get_header('User-agent'))

response = urlopen(request)

info = response.read()
print(info.decode())














