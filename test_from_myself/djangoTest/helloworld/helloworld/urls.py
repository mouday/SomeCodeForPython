"""helloworld URL Configuration

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
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
from . import testdb
from . import search
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^hello$', views.hello),
    url('^sayhello$', views.sayhello),
    url('^label$', views.label),
    url('^child$', views.child),
    url('^insertdb$', testdb.insertdb),
    url('^getbd$', testdb.getdb),
    url('^updatedb$', testdb.updatedb),
    url('^deletedb$', testdb.deletedb),
    url('^search$', search.search),
    url('^search_form$', search.search_form),
    url('^search-post$', search.search_post),

]
