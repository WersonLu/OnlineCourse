# encoding: utf-8
# !/usr/bin/env python


'''
@author  : wersonliu
@File    : urls.py
@data    : 
'''
from django.conf.urls import url, include
from .views import OrgListView,AddUserAsk

urlpatterns = [
    url(r'^list/$', OrgListView.as_view(), name="org_list"),
    url(r'^add_ask/$',AddUserAsk.as_view(),name="add_ask"),
]
