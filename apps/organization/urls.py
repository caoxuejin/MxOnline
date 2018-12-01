# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 20:48
# @Author  : caoxuejin
# @Email   : 1282911984@qq.com
# @File    : urls.py
# @Software: PyCharm


from django.conf.urls import url
from organization.views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, \
    AddFavView, TeacherListView, TeacherDetailView

urlpatterns = [
    # 课程机构列表
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    # 用户咨询
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
    # 机构首页
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    # 机构课程
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),
    # 机构介绍
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    # 机构教师
    url(r'^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),

    # 机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),

    # 课程讲师列表
    url(r'^teacher/list/$', TeacherListView.as_view(), name="teacher_list"),

    # 课程讲师详情
    url(r'^teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name="teacher_detail")
]
