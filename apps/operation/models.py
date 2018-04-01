# encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from users.models import UserProfile

from courses.models import Course


# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"咨询用户名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机号")
    # 此时用户不知道有什么课程,所有并没有对课程的外键
    course = models.CharField(max_length=50, verbose_name=u"咨询什么课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"评论人")
    course = models.ForeignKey(Course, verbose_name=u"被评论的课程")
    comments = models.CharField(max_length=200, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.ImageField(default=0, verbose_name=u"数据id")
    fav_type = models.ImageField(choices=((1, u"课程"), (2, u"课程名"), (3, u"讲师")), default=1, verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.ImageField(default=0, verbose_name=u"接受用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")

    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


# 用户学习的课程记录
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name
