"""testwork1 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import django
from django.contrib import admin
from django.urls import path,re_path
import testwork1.views as views
from . import chatgpttest
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import url ##新增
# from django.conf.urls import url ##新增
# 部署上线后path需要改为re_path
urlpatterns = [
    path("admin/", admin.site.urls),
    path("bootstrap.css",chatgpttest.cssres),#css文件
    path("chatui/",chatgpttest.res),
    path("",views.main),
    path('main/',views.main,name='main'),
    path('Login/',views.Login,name='Login'),
    path('Login/verification_code/',views.verification_code, name='verification_code'),
    path("reg_msg/",views.register_process),
    path("log_check/",views.Login),
    path('register/',views.register,name='register'),
    path('register/verification_code/',views.verification_code, name='verification_code'),
    path("get_username/",views.user_name),
    path("logout/",views.log_out),
    path("chatui/get_history/",views.get_history),
    path("get_history/",views.get_history)
]
urlpatterns += staticfiles_urlpatterns()
#本文件负责配置url和视图函数的对应关系