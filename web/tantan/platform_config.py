'''
各个第三方平台的接入配置
'''

# 互亿无限短信配置
HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': 'C42331298',
    'password' : '2d2284b74dc4972da3df3915fb17b28f',
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile': None,
    'format':'json'
}
