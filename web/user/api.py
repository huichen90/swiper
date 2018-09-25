from django.shortcuts import render
from django.views.decorators.http import require_POST

from common import rds
from common import errors
from user.models import User
from user.logic import send_login_code


@require_POST
def verify_phone(request):
    '''提交手机号，向用户发送验证码'''
    phone_num = request.POST.get('phone')
    send_login_code(phone_num)


@require_POST
def verify_code(request):
    phone_num = request.POST.get('phone')
    code = request.POST.get('code')
    key = keys.LOGIN_SMS % phone_num
    if rds.get(key) != code:
        raise errors.InvalidPIN

    user, created = User.objects.get_or_create(phone_num=phone_num)
    if created:
        user.init()
    return user.to_dict()


@require_POST
def setup(request):
    pass
