# encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.

# 课程机构,老师信息
# @python_2_unicode_compatible
from future.utils import python_2_unicode_compatible


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市名")
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名")
    desc = models.TextField(verbose_name=u"机构描述")
    category = models.CharField(verbose_name="机构类别", default="pxjg", max_length=20,
                                choices=(("pxjg", '培训机构'), ('gr', '个人'), ('gx', '高校')))
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"机构封面图")
    address = models.CharField(max_length=150, verbose_name=u"地址")
    city = models.ForeignKey(CityDict, verbose_name=u"所在城市")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    students = models.IntegerField(verbose_name='学习人数', default=0)
    course_nums = models.IntegerField(verbose_name='课程数', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    name = models.CharField(max_length=50, verbose_name=u"教师名字")
    work_year = models.CharField(default=0, verbose_name=u"工作年限", max_length=10)
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    def __str__(self):
        return self.name

    # def __init__(self):
    #     return self.name

    class Meta:
        verbose_name = u"教师信息"
        verbose_name_plural = verbose_name
