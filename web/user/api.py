from django.shortcuts import render
from django.views.decorators.http import require_POST

from user.logic import send_login_code


@require_POST
def verify_phone(request):
    '''提交手机号，向用户发送验证码'''
    phone_num = request.POST.get('phone')
    send_login_code(phone_num)


@require_POST
def verify_code(request):
    pass


def setup(request):
    pass
