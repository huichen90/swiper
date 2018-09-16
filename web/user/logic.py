from common import rds
from common import sms
from common import keys
from common import errors


def send_login_code(phone_num):
    '''发送登陆验证短信'''
    # TODO: 接入 celery 异步发送短信
    key = keys.LOGIN_SMS % phone_num
    if not rds.exists(key):
        random_code = sms.gen_verify_code(4)
        send_sms(phone_num, random_code)
        rds.setex(key, random_code, 60)  # 状态码有效期 60s
    else:
        raise errors.NotYetTime
