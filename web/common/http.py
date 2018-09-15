from json import dumps

from common.errors import OK
from django.conf import settings
from django.http import HttpResponse


def render_json(data=None, error=OK) -> HttpResponse:
    '''将返回值渲染为 JSON 数据'''
    result = {'data': data, 'status': error.code}

    if settings.DEBUG:
        json_str = dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_str = dumps(result, ensure_ascii=False, separators=[',', ':'])

    return HttpResponse(json_str)
