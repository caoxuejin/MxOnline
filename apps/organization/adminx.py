# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 23:04
# @Author  : caoxuejin
# @Email   : 1282911984@qq.com
# @File    : adminx.py
# @Software: PyCharm


import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ["name", "desc", "add_time"]
    search_fields = ["name", "desc"]
    list_filter = ["name", "desc", "add_time"]


class CourseOrgAdmin(object):
    list_display = ["name", "desc", "click_nums", "fav_nums", "image", "address", "city", "add_time"]
    search_fields = ["name", "desc", "click_nums", "fav_nums", "image", "address", "city"]
    list_filter = ["name", "desc", "click_nums", "fav_nums", "image", "address", "city__name", "add_time"]
    # 外键对应的select下拉框数据过大时加载很慢，设置为搜索模式
    refield_style = "fk-ajax"


class TeacherAdmin(object):
    list_display = ["org", "name", "work_years", "work_company", "work_position", "points", "click_nums", "fav_nums",
                    "add_time"]
    search_fields = ["org", "name", "work_years", "work_company", "work_position", "points", "click_nums", "fav_nums"]
    list_filter = ["org__name", "name", "work_years", "work_company", "work_position", "points", "click_nums",
                   "fav_nums", "add_time"]


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
