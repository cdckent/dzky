# -*- coding:utf-8 -*-

import yaml

class ReadConfig():
    data = None

    def __init__(self):
        with open('./config/data.yml' , 'r') as file:
            self.data = yaml.load(file.read(), Loader=yaml.FullLoader)
    '''' 获取yaml文件可读；直接将文件读取的放入到yaml.load()方法中'''
    
    def read_SQL_config(self, SQL_name):
        return self.data.get('SQL').get(SQL_name)

    def read_webtest_config(self, webtest_name):
        return self.data.get('webtest').get(webtest_name)
rc=ReadConfig()

if __name__ == '__main__':
    print(rc.read_SQL_config('host'))
    print(rc.read_webtest_config('host'))