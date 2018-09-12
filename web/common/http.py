from json import dumps

from django.conf import settings
from django.http import HttpResponse


def render_json(data):
    if settings.DEBUG:
        json_str = dumps(data, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_str = dumps(data, ensure_ascii=False, separators=[',', ':'])

    return HttpResponse(json_str)
