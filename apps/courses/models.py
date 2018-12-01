# _*_ coding:utf-8 _*_

from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField
from organization.models import CourseOrg, Teacher


# Create your models here.


class Course(models.Model):
    """
    课程
    """
    # 课程名称
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    # 课程机构
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True, on_delete=models.CASCADE)
    # 课程描述
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    # 课程详情
    detail = UEditorField(verbose_name=u"课程详情", width=600, height=300, imagePath="courses/ueditor/",
                          filePath="courses/ueditor/", default='')
    # 是否轮播
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    # 讲师
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=u"讲师", null=True, blank=True)
    # 难易程度
    degree = models.CharField(choices=(("primary", "初级"), ("intermediate", "中级"), ("advanced", "高级")),
                              verbose_name=u"难易程度", max_length=15)
    # 学习时长
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    # 学习人数
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    # 收藏人数
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    # 封面图
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图")
    # 点击数
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    # 课程类别
    category = models.CharField(default=u"后端开发", max_length=20, verbose_name=u"课程类别")
    # 课程标签
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)
    # 课程须知
    youneed_know = models.CharField(default="", max_length=300, verbose_name=u"课程须知")
    # 老师告诉你
    teacher_tell = models.CharField(default="", max_length=300, verbose_name=u"老师告诉你")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 获取课程章节数
        return self.lesson_set.all().count()

    get_zj_nums.short_description = "章节数"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.projectsedu.com'>跳转</a>")

    go_to.short_description = "跳转"

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程所有章节
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    """
    章节
    """
    # 课程
    course = models.ForeignKey(Course, verbose_name=u"课程", on_delete=models.CASCADE)
    # 章节名
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_lesson_video(self):
        # 获取章节视频
        return self.video_set.all()


class Video(models.Model):
    """
    视频
    """
    # 章节
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节", on_delete=models.CASCADE)
    # 视频名
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    # 学习时长
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    # 访问地址
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    """
    课程资源
    """
    # 课程
    course = models.ForeignKey(Course, verbose_name=u"课程", on_delete=models.CASCADE)
    # 名称
    name = models.CharField(max_length=100, verbose_name=u"名称")
    # 资源文件
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
