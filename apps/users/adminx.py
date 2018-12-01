# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 23:58
# @Author  : caoxuejin
# @Email   : 1282911984@qq.com
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from xadmin import views

from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    # 设置主题
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "麻花屋后台管理系统"
    site_footer = "麻花屋在线网"
    # 左侧导航栏显示样式
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ["code", "email", "send_type", "send_time"]
    search_fields = ["code", "email", "send_type"]
    list_filter = ["code", "email", "send_type", "send_time"]


class BannerAdmin(object):
    list_display = ["title", "image", "url", "index", "add_time"]
    search_fields = ["title", "image", "url", "index"]
    list_filter = ["title", "image", "url", "index", "add_time"]


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
