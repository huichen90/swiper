import random

import requests

from tantan import platform_config


def gen_verify_code(length=4):
    '''生成验证码'''
    if length <= 0:
        length = 1
    code = random.randrange(10 ** (length - 1), 10 ** (length))
    return str(code)


def send_sms(phone_num, text):
    '''发送短信'''
    params = platform_config.HY_SMS_PARAMS.copy()
    params['mobile'] = phone_num
    params['content'] = params['content'] % text
    headers = {
        "Accept": "text/plain",
        "Content-type": "application/x-www-form-urlencoded"
    }
    response = requests.post(platform_config.HY_SMS_URL, data=params, headers=headers)
    return response
