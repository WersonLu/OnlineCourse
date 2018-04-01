# encoding: utf-8
# !/usr/bin/env python


'''
@contact: wersonliugmail.com
@File    : adminx.py
'''
import xadmin
from .models import Course, Lesson, Video, CourseResoure


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'len_times', 'students', 'fav_nums', 'image', 'click_num',
                    'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'len_times', 'students', 'fav_nums', 'image', 'click_num', ]

    list_filter = ['name', 'desc', 'detail', 'degree', 'len_times', 'students', 'fav_nums', 'image', 'click_num',
                   'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # 外键搜索处理办法
    list_filter = ['course', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResoure, CourseResourceAdmin)
