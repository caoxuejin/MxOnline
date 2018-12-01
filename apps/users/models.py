# _*_ coding:utf-8 _*_

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    """
    用户信息
    """
    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default=u"")
    # 生日
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    # 性别
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default=u"female")
    # 区域
    address = models.CharField(max_length=100, default=u"", verbose_name=u"区域")
    # 手机号
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机号")
    # 用户头像
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def unread_nums(self):
        # 获取未读消息的数量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    """
    邮箱验证码
    """
    # 验证码
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    # 邮箱
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # 发送类型
    send_type = models.CharField(choices=(("register", u"注册"), ("forget", u"找回密码"), ("update_email", u"修改邮箱")),
                                 max_length=30, verbose_name=u"验证码类型")
    # 发送时间
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}({1})".format(self.code, self.email)


class Banner(models.Model):
    """
    轮播图
    """
    # 标题
    title = models.CharField(max_length=100, verbose_name=u"标题")
    # 轮播图
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    # 访问地址
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    # 顺序
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
