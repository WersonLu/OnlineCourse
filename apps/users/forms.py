# encoding: utf-8
# !/usr/bin/env python


'''
@author  : wersonliu
@File    : forms.py
@data    : 
'''
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # 必须要与html表单字段的name一样
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 忘记密码
class ForGetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 修改密码
class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)
