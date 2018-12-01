# _*_ coding:utf-8 _*_

from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course

# Create your models here.


class UserAsk(models.Model):
    """
    用户咨询
    """
    # 姓名
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    # 手机号
    mobile = models.CharField(max_length=11, verbose_name=u"手机号")
    # 课程名称
    course_name= models.CharField(max_length=50, verbose_name=u"课程名")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    """
    课程评论
    """
    # 用户
    user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    # 课程
    course = models.ForeignKey(Course, verbose_name=u"课程", on_delete=models.CASCADE)
    # 评论
    comments = models.CharField(max_length=200, verbose_name=u"评论")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    """
    用户收藏
    """
    # 用户
    user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    # 数据ID
    fav_id = models.IntegerField(default=0, verbose_name=u"数据ID")
    # 收藏类型
    fav_type = models.IntegerField(choices=((1, "课程"), (2, "课程机构"), (3, "讲师")), verbose_name=u"收藏类型")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    """
    用户消息
    """
    # 接收用户
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    # 消息内容
    message = models.CharField(max_length=500, verbose_name=u"消息内容")
    # 是否已读
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    """
    用户课程
    """
    # 用户
    user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    # 课程
    course = models.ForeignKey(Course, verbose_name=u"课程", on_delete=models.CASCADE)
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name

