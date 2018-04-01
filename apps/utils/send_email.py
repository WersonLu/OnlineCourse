# encoding: utf-8
# !/usr/bin/env python


'''
@author  : wersonliu
@File    : send_email.py
@data    : 
'''
from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from OnLineCourse.settings import EMAIL_FROM


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = generate_random_str(9)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "请点击链接激活账号：http://127.0.0.1:8000/active/{0}".format(code)

        # 发送标题，正文，来源，去处
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type=="forget":
        email_title = "密码重置链接"
        email_body = "请点击链接重置密码：http://127.0.0.1:8000/reset/{0}".format(code)


def generate_random_str(randomlength=8):
    str = ''
    chars = 'ABCDEFGabcdefg0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str
