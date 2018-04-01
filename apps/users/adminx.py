# encoding: utf-8
# !/usr/bin/env python


'''
@contact: wersonliugmail.com
@File    : adminx.py
'''
import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


# from django.db import models
# from datetime import datetime

class BaseSetting(object):
    enable_themes = True
    user_bootswatch = True


class GlobalSetting(object):
    site_title = "信息院-在线教育"
    site_footer = "信息咨询研究院"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    # 后台详情列表页显示字段
    # 展示
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# 主题
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
