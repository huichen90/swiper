"""tantan URL Configuration

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


urlpatterns = [
    url(r'^user/verify$', user_api.verify_phone),
    url(r'^user/login$', user_api.login),
    url(r'^user/profile/show$', user_api.show_profile),
    url(r'^user/profile/update$', user_api.update_profile),
    url(r'^user/avatar/upload$', user_api.upload_avatar),
]
