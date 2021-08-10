import requests


class BaseReq:
    Response = requests.Response

    def get(self, url, params=None, **kwargs):
        self.Response = requests.get(url, params=params, **kwargs)
        return self

    def post(self, url, data=None, json=None, **kwargs):
        self.Response = requests.post(url, data=data, json=json, **kwargs)
        return self

    def put(self, url, data=None, **kwargs):
        self.Response = requests.put(url, data=data, **kwargs)
        return self

    def delete(self, url, **kwargs):
        self.Response = requests.delete(url, **kwargs)
        return self

    # 断言方法 可以扩展增加
    def assert_eq(self, filed: str, expected):
        res = self.Response.json()
        if filed.find("_") != -1:
            realValue = self.get_param_by_hierarchy(filed, res)
        else:
            realValue = res[filed]
        if realValue == expected:
            print("断言成功")
            return self
        print(f"断言失败, 预期值{expected} 不等于 实际值: {realValue}")
        return self

    def get_param_by_hierarchy(self, hierarchyStr: str, dictParamMap: dict) -> object:
        """

        通过层级关系获得值
        :param hierarchyStr: 层级关系字符串
        :param dictParamMap: 目标字典
        :return:
        """
        hierarchyObj = object
        h = Hierarch(dictParamMap)
        filedList = hierarchyStr.split("_")
        lastFiled = filedList.pop()
        for i in filedList:
            filedStr = str(i)
            if filedStr.isdigit():
                index = int(filedStr)
                hierarchyObj = h.getList(index)
                continue
            if filedStr == "-1":
                index = -1
                hierarchyObj = h.getList(index)
                continue
            hierarchyObj = h.getDict(filedStr)
        value = hierarchyObj.getValueByDict(lastFiled)
        return value
