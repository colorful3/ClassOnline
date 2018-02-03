# -*- coding: utf8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from users.models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from util.email_send import send_register_mail


# Create your views here.

"""
    define a class, Django will auto run this authenticate,to reload the function named authenticate,
    you can write some logic in the function
"""


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # Using the function Q to get the union set. '|' means 'OR', ',' means 'AND'
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    # 验证邮箱，激活用户
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form, 'method':'register'})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {
                    'register_form': register_form,
                    'msg': '用户已经存在',
                    'method': 'register'
                })
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()

            # 发送激活连接的邮件
            send_register_mail(user_name, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {
                'register_form': register_form,
                'method': 'register',
            })


class LoginView(View):
    # 重新定义父类的get方法
    def get(self, request):
        return render(request, 'login.html', {})

    # 重新定义父类的post方法
    def post(self, request):
        # receive the http request post params
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        redirect_url = request.POST.get('redirect_url') if request.POST.get('redirect_url') else 'http://127.0.0.1:8000'
        # 实例化LoginForm类
        login_form = LoginForm(request.POST)
        # 使用form验证，验证通过返回True，否则返回False，验证失败后，错误信息在login_form._errors中，是一个字典
        if login_form.is_valid():
            # check the user_name and pass_word, if the check is credential, return a User object
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active is not True:
                    return render(request, 'login.html', {'msg': 'User is not active'})
                login(request, user)
                return redirect(redirect_url)
                # return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


# 申请找回密码
class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetPwdForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        email = request.POST.get('email', '')
        # To valid the form params
        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid():
            send_register_mail(email, send_type='forget')
            return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {
                'forget_form': forget_form,
            })


# 重置密码的页面
class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email, 'msg': '两次输入密码不一致'})
            # 根据email修改密码
            user = UserProfile.objects.filter(email=email).get()
            user.password = make_password(pwd2)
            user.save()

            return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'modify_form': modify_form, 'email': email})


"""
    def user_login(request):
        if request.method == 'POST':
            # receive the http request post params
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            # check the user_name and pass_word, if the check is credential, return a User object
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active is not False:
                    return render(request, 'login.html', {'msg': 'User is not active'})
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        elif request.method == 'GET':
            return render(request, 'login.html', {})    
"""
