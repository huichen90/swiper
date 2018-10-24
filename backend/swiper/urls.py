"""swiper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from user import api as user_api
from social import api as social_api
from vip import api as vip_api


urlpatterns = [
    # User API
    url(r'^user/verify$', user_api.verify_phone),
    url(r'^user/login$', user_api.login),
    url(r'^user/profile/show$', user_api.show_profile),
    url(r'^user/profile/update$', user_api.update_profile),
    url(r'^user/avatar/upload$', user_api.upload_avatar),

    # Social API
    url(r'social/recommend$', social_api.recommend),
    url(r'social/like$', social_api.like),
    url(r'social/superlike$', social_api.superlike),
    url(r'social/dislike$', social_api.dislike),
    url(r'social/rewind$', social_api.rewind),
    url(r'social/likedme$', social_api.who_liked_me),
    url(r'social/friends$', social_api.friend_list),
    url(r'social/break_off$', social_api.break_off),

    # VIP API
    url(r'vip/info$', vip_api.vip_info),
]
