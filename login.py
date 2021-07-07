import json
import requests
from random import randint
from 工具 import Tool


class My_request(object):

    # token函数 调用函数就可获取token值 再用到新增接口
    def get_token(self):
        # 获取token
        p = Tool().decode('123123')
        token_urls ='https://test.zhihuiyunxing.com/api/v1/manage/login'
        payload = {'phone': 13000000000, 'password': p, 'formKey': '4ji3EvuwNziPKF8QXqXMTukGqPmlwOFJ', 'organizationId': 1}
        # print(payload)
        header_token = {'Content-Length': '149', 'Content-Type': 'application/x-www-form-urlencoded'}

        # 发送请求 json 请求体
        # res = requests.post(token_urls, json=payload)
        # data表单格式比较麻烦
        res = requests.post(token_urls,data=payload,headers= header_token)
        # 返回响应数据 输出字符串格式
        # json.loads() 把字符串 转为字典对象 再通过键取值
        # return json.loads(res.text)['token']

        # 本身是字典形式的话 直接 .JSON
        # 返回json 字典格式
        # print(res.json())
        return res.json()['data']['token']

if __name__ == '__main__':
    m  = My_request()
    m.get_token()
    print(m.get_token())