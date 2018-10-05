from django.shortcuts import render

from lib.cache import rds
from common import errors
from common.http import require_post
from user.models import User
from user.logic import send_login_code


@require_post
def verify_phone(request):
    '''提交手机号，向用户发送验证码'''
    phone_num = request.POST.get('phone')
    send_login_code(phone_num)


@require_post
def verify_code(request):
    '''提交验证码'''
    phone_num = request.POST.get('phone')
    code = request.POST.get('code')
    key = keys.LOGIN_SMS_KEY % phone_num
    if rds.get(key) != code:
        raise errors.InvalidPIN

    user, created = User.get_or_create(phone_num=phone_num)
    if created:
        user.init()
    return user.to_dict()


@require_post
def set_profile(request):
    '''修改用户配置'''
    pass
