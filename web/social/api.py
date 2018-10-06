from django.shortcuts import render

from common.http import require_post
from social import logic


@require_post
def like(request):
    '''喜欢'''
    stranger_id = int(request.POST.get('stranger_id'))
    return logic.like(stranger_id)


@require_post
def superlike(request):
    '''超级喜欢'''
    stranger_id = int(request.POST.get('stranger_id'))
    return logic.superlike(stranger_id)


@require_post
def dislike(request):
    '''不喜欢'''
    stranger_id = int(request.POST.get('stranger_id'))
    return logic.dislike(stranger_id)


@require_post
def rewind(request):
    '''反悔'''
    stranger_id = int(request.POST.get('stranger_id'))
    return logic.rewind(stranger_id)


@require_post
def stepup(request):
    '''增加曝光率'''
    return logic.stepup()
