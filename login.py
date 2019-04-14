import requests,json
request=requests.session()
class Login():
    def __init__(self):
        self.headers={'Host':'h5.ele.me',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Accept':'*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding':'gzip, deflate, br',
        'Referer':'https://h5.ele.me/login/',
        'content-type':'application/json; charset=utf-8',
        'origin':'https://h5.ele.me',
        'Content-Length':'72',
        'Connection':'keep-alive',
        'TE':'Trailers',}
        self.phone=input('手机号：')
    def send(self):
        url='https://h5.ele.me/restapi/eus/login/mobile_send_code'
        patload={"mobile":self.phone,"captcha_value":"","captcha_hash":"","scf":"ms"}

        response=requests.post(url,headers=self.headers,data=json.dumps(patload))

        token=json.loads(response.text)['validate_token']

        code=input('验证码：')
        self.login(code,token)

    def login(self,code,token):

        url='https://h5.ele.me/restapi/eus/login/login_by_mobile'
        payload={"mobile":self.phone,"validate_code":str(code),
                 "validate_token":str(token),
                 "scf":"ms"}

        response = request.post(url, headers=self.headers, data=json.dumps(payload))
        if 'user_id' in str(response.text):
            print('登陆成功！')
        else:
            print('登陆异常！')
        with open('cookies.txt','w')as f:
            f.write(str(request.cookies['SID'])+'\n'+str(request.cookies['USERID'])+'\n'+str(request.cookies['UTUSER'])+'\n'+str(request.cookies['track_id']))
if __name__ == '__main__':
    L=Login()
    L.send()
