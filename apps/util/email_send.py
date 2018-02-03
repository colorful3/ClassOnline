# -*- coding: utf8 -*-
__author__ = 'Colorful'
__date__ = '2018/1/25 上午12:02'
from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from py2dj.settings import EMAIL_FROM
from random import randint

"""
    随机生成字符串函数
"""


def random_str(random_length=8):
    str1 = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    # 列表解析
    length = len(chars) - 1
    for i in range(random_length):
        str1 += chars[randint(0, length)]
    return str1


# 发送邮件方法
def send_register_mail(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email=email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title = '慕学网在线网注册激活连接'
        email_body = '请点击下面的连接激活你的账号：<a target="_blank" href="http://127.0.0.1:8000/active/{0}'.format(code)\
                     + '">连接</a>'
    elif send_type == 'forget':
        email_title = '慕学网在线网密码重置连接'
        email_body = '请点击下面的连接激活你的账号：<a target="_blank" href="http://127.0.0.1:8000/reset/{0}'.format(code) \
                     + '">连接</a>'
        send_status = send_mail(subject=email_title, message=email_body, from_email=EMAIL_FROM, recipient_list=[email])
        if send_status:
            pass



