from django.shortcuts import render
from django.views.decorators.http import require_POST

from social import helper


@require_POST
def like(request):
    '''喜欢'''
    stranger_id = int(request.POST.get('stranger_id'))
    return helper.like(stranger_id)


@require_POST
def superlike(request):
    '''超级喜欢'''
    stranger_id = int(request.POST.get('stranger_id'))
    return helper.superlike(stranger_id)


@require_POST
def dislike(request):
    '''不喜欢'''
    stranger_id = int(request.POST.get('stranger_id'))
    return helper.dislike(stranger_id)


@require_POST
def rewind(request):
    '''反悔'''
    stranger_id = int(request.POST.get('stranger_id'))
    return helper.rewind(stranger_id)


@require_POST
def stepup(request):
    '''增加曝光率'''
    return helper.stepup()
