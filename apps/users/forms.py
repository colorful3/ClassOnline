# -*- coding: utf8 -*-
__author__ = 'Colorful'
__date__ = '2018/1/24 下午2:02'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=5, max_length=20)
    password = forms.CharField(required=True, min_length=5, max_length=20)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5, max_length=20)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5, max_length=20)
    password2 = forms.CharField(required=True, min_length=5, max_length=20)
