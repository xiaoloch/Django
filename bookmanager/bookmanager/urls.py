"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.urls import converters
from django.urls.converters import register_converter
from book.views import register,header,json,set_cookie,get_cookie,del_cookie,set_session,get_session,login,loginview
# from book.views import index

class Mobile():
    regex = '1[3-9]\d{9}'
    def to_python(self,value):
        return int(value)

register_converter(Mobile,'phone')

urlpatterns = [
    path('admin/', admin.site.urls),
    # 添加一个路径
    # path('路由','视图函数名')
    # path('<int:para1>/',include('book.urls')),
    path('register/',register),
    path('header/',header),
    path('resp/', json),
    path('set_cookie',set_cookie),
    path('get_cookie',get_cookie),
    path('del_cookie',del_cookie),
    path('set_session',set_session),
    path('get_session',get_session),
    path('163login',login.as_view()),
    path('authlogin',loginview.as_view()),
]

