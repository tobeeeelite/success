# encoding:utf-8
import requests
import json
import base64
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=GKHIEq6gVOfp2AeRxfUopSDM&client_secret=dLrlMlGemQ1oan2OS8GogLDD0dt1HuVI'
response = requests.get(host)
if response:
    print(response.json())
request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/multi_object_detect"
# 二进制方式打开图片文件
f = open('0.jpg','rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '[24.5fda1f940f169efe2204ab7e4d34bc86.2592000.1619678721.282335-23899102]'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())