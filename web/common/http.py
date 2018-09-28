from json import dumps

from common.errors import OK
from django.conf import settings
from django.http import HttpResponse


def render_json(data=None, error=OK) -> HttpResponse:
    '''将返回值渲染为 JSON 数据'''
    result = {
        'data': data or error.data,
        'sc': error.code  # 状态码 (status code)
    }

    if settings.DEBUG:
        # Debug 模式时，按规范格式输出 json
        json_str = dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        # 正式环境下，将返回数据压缩
        json_str = dumps(result, ensure_ascii=False, separators=[',', ':'])

    return HttpResponse(json_str)
