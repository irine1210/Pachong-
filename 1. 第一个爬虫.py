'''
@Author  : heyheyheyJoy
@Time    : 2022/3/13 8:06 下午
@File    : 1. 第一个爬虫.py
'''

from urllib.request import *

url = "http://www.baidu.com"

# 发送请求
response = urlopen(url)

# 读取内容
info = response.read()

# 打印内容
#print(info.decode())

# 打印状态码
print(response.getcode())

# 打印真实url
print(response.geturl())

# 打印响应头
print(response.info())