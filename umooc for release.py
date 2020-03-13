import requests
import datetime


class umooc:
    def __init__(self):
        self.__username = "学号"
        self.__password = "将你密码MD5输入，需为小写MD5"
        self.cookies = {}
        self.login_status = 0
        self.headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; GA01187 Build/QKQ1.190716.003)",
            'Authorization': 'OAuth2: token'
        }
        self.successs = []
        self.error = []
        print('umooc8 automatic sign')

    def login(self):
        '''登录并获取cookie'''
        login_url1 = "http://e-learning.cqmu.edu.cn/mobile/getSessionId.do"
        login_url2 = "http://e-learning.cqmu.edu.cn/mobile/login_check.do"
        params = {
            'deviceUuid': "b2818266aba9625c",
            'appVersion': "8.5.2",
            'j_password': self.__password,
            'devicePlatform': "Android",
            'deviceVersion': "10",
            'j_username': self.__username,
            'deviceName': "GA01187"
        }
        try:
            res1 = requests.post(login_url1, headers=self.headers, params=params, timeout=5)
            self.cookies = res1.cookies
            res2 = requests.post(login_url2, headers=self.headers, params=params, timeout=5)
            if True:
                self.cookies = res1.cookies
                self.login_status = 1
                print("login success")
                print(res2.text)
                #return True
            else:
                self.cookies = {}
                print(res2.text("errorMsg"))
        except Exception as e:
            print("fail,reason：", e)
            return None

    def sign(self):
        '''此处为签到部分'''
        sign_url = "http://e-learning.cqmu.edu.cn/mobile/此处输入签到二维码使用其他软件扫描后的链接"
        params = {
            'context': "自行获取填写，这个是课程ID，即你访问课程时URL中的courseId",
            'id': "自行抓包获取，在包中扫码签到时显示ID，在抓包课程活动时显示为parentID",
        }
        res3 = requests.post(sign_url, headers=self.headers, params=params, timeout=5)
        print(res3.text)
        requests.get('https://sc.ftqq.com/你的SCKEY.send',params=dict(text='自己瞅眼签到成功没.', desp=res3.text))

example = umooc()
example.login()
example.sign()