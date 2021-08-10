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

    # ���Է��� ������չ����
    def assert_eq(self, filed: str, expected):
        res = self.Response.json()
        if filed.find("_") != -1:
            realValue = self.get_param_by_hierarchy(filed, res)
        else:
            realValue = res[filed]
        if realValue == expected:
            print("���Գɹ�")
            return self
        print(f"����ʧ��, Ԥ��ֵ{expected} ������ ʵ��ֵ: {realValue}")
        return self

    def get_param_by_hierarchy(self, hierarchyStr: str, dictParamMap: dict) -> object:
        """

        ͨ���㼶��ϵ���ֵ
        :param hierarchyStr: �㼶��ϵ�ַ���
        :param dictParamMap: Ŀ���ֵ�
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
