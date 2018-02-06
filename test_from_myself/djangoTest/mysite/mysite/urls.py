"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.conf.urls import url
from . import view

# 正则使用原样字符串，以r开头
urlpatterns = [
    url(r'^$', view.index),    # 空字符串，指向主页
    url(r'^hell$', view.hello),
    url(r'^time$', view.show_time),
    url(r'^date$', view.show_date),
    url(r'^timepage$', view.show_current_datetime),
    url(r'^time/(\d{1,2})$', view.show_datetime),   # 括号括起来的内容会被传递到函数
    url(r'^test$', view.test),
    url(r'^showtime$', view.shortcuts_test),
    url(r'^name_list$', view.name_list),

]