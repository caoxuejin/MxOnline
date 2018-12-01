"""Mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve

from users.views import LoginView, LogOutView, RegisterView, ForgetPwdView, ResetView, ModifyPwdView, IndexView, ActiveUserView
from Mxonline.settings import MEDIA_ROOT

urlpatterns = [
    url(r'xadmin/', xadmin.site.urls),

    url(r'^$', IndexView.as_view(), name="index"),
    # url(r'^login/$', user_login, name="login")
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogOutView.as_view(), name="logout"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    # 用户激活
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    # 课程机构url配置
    url(r'^org/', include(('organization.urls', 'organization'), namespace="org")),

    # 课程相关url配置
    url(r'^course/', include(('courses.urls', 'courses'), namespace="course")),

    # 配置上传文件的访问处理函数
    # 开发
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 生产
    # url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),

    # 个人中心URL
    url(r'^users/', include(('users.urls', 'users'), namespace="users")),

    # 富文本相关url
    url(r"^ueditor/", include(("DjangoUeditor.urls", "ueditor"), namespace="ueditor"))

]

# 全局404和500页面配置
handler404 = 'users.views.page_not_found'
handler500 = "users.views.page_error"
