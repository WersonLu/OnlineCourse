# encoding: utf-8
# !/usr/bin/env python


'''
@author  : wersonliu
@File    : forms.py
@data    : 
'''
from django import forms
import re

from operation.models import UserAsk


# 1.传统写法
# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     phone = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, max_length=50, min_length=5)


# 2.modelform 写法

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk

        fields = ['name', 'mobile', 'course']

    def clead_mobile(self):
        """
        手机号验证
        :return:
        """
        mobile = self.cleaned_data['moblie']
        REGEX_MOBILE = "1[358]\d{9}$|^147\d{8}|^176\d{8}$"
        p=re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法",code="mobile_invalde")