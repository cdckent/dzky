import hashlib
import requests
import json
from login import My_request
import config
import unittest
from readyml import ReadConfig
rc=ReadConfig()
host = rc.read_webtest_config('host')

class Register(My_request):
    def __init__(self):
        self.token = My_request().get_token()
        self.header_addusr = {'Content-Type': 'application/x-www-form-urlencoded', 'token': '%s' % self.token}

        # 发送请求 url 请求体
        # res = requests.get(self.addUsr_url, headers=self.header_addusr)
        # print(res.text)

        # 查看发出去的请求： fiddler，print打印
        # 查看请求头
        # print(res.request.headers)

        # 引入完美打印
        # import pprint
        # pprint.pprint(res.text())

    def test001(self):#获取所有线路排班
        r=requests.get(url= host+ 'manage/line/scheduling?organizationId=&lineType=&startStationName=&endStationName=&schedulingType=', headers=self.header_addusr)
        print(r.text)
        c = unittest.TestCase()

    def test002(self):#添加ID（371） 线路的排班
        data= {"lineId": 371,
               "schedulingJson": '[{"schedulingTime":1618243200,"shift":[{"status":1,"startTime":"20:30","endTime":"20:31","ticketNumType":2,"soldTickets":"","ticketNum":6,"isEnabled":1,"compile":true,"operationType":2,"schedulingTime":1618243200,"schedulingVehicleJson":[{"id":63,"created":1615528278,"updated":1615528278,"version":null,"organizationName":"智慧云行","organizationId":1,"vehicleId":63,"licenseNo":"贵C66666","vehicleSeat":7,"driverId":110,"driverName":"ty","driverPhone":"15000000000","vehicleSeatAndFeeVos":[{"seatNo":"A座","fee":1,"id":null},{"seatNo":"B座","fee":1,"id":null},{"seatNo":"C座","fee":1,"id":null},{"seatNo":"D座","fee":1,"id":null},{"seatNo":"E座","fee":1,"id":null},{"seatNo":"F座","fee":1,"id":null}]}]}]}]'
}
        r=requests.post(url= host+ "manage/line/scheduling", data=data, headers=self.header_addusr)
        print(r.text)

Register().test001()

