# -*-coding:utf-8-*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ForGetForm, ModifyPwdForm
from django.contrib.auth.hashers import make_password
from utils.send_email import send_register_email


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # q 并集查询
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # 检查加密的密码
            if user.check_password(password):
                return user
        except Exception as e:
            return None


#
# class ActiveUserView(View):
#
#     def get(self, request, active_code):
#         all_records = EmailVerifyRecord.objects.filter(code=active_code)
#         if all_records:
#             for record in all_records:
#                 email = record.email
#                 user = UserProfile.objects.get(email=email)
#                 user.is_active = True
#                 user.save()
#             return render(request, 'login.html')
#         else:
#             return render(request, 'active_fail.html')

class ActiveUserView(View):
    # 用户点击激活链接，url提取activecode，用get获取login页面
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")

        return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    # 用户执行注册表单操作
    def post(self, request):
        # 1,取到用户post的数据
        register_form = RegisterForm(request.POST)
        # 如果数据合法有效
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            # 查询用户是存在的,返回注册页并回填用户注册的数据
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {"register_form": register_form, "msg": u"用户已经存在"})
            pass_word = request.POST.get("password", "")
            # 实例化一个用户模型
            user_profile = UserProfile()
            # 把前台取到的值赋给用户模型里的username属性
            user_profile.username = user_name

            user_profile.email = user_name
            # 用户刚注册,默认用户未激活状态
            user_profile.is_active = False
            # 存储加密的密码
            user_profile.password = make_password(pass_word)
            # 保存用户
            user_profile.save()
            # 发送给用户注册时用的邮件
            send_register_email(user_name, "register")
            # 完成整个页面返回登录页面
            return render(request, 'login.html')
        else:
            # 否则数据无效继续在注册页面
            return render(request, 'register.html', {"register_form": register_form})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 数据合法走下面
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")

            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # 如果登录用户不为空,且激活,则登录
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')  # 把请求结果返回
                else:
                    # 否则返回登录页并提示
                    return render(request, 'login.html', {"msg": u"用户未激活"})
                # print('success')
            # 数据格式合法但不正确走下面
            else:
                return render(request, "login.html", {"msg": u"用户名或者密码错误", "login_form": login_form})
        else:
            return render(request, "login.html", {"login_form": login_form})  #


class ForgetPwdView(View):

    def get(self, request):
        forget_form = ForGetForm()
        return render(request, 'forgetpwd.html', {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForGetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            send_register_email(email, "forget")
            return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {"forget_form": forget_form})


class ResetUserView(View):
    # 用户点击激活链接，url提取activecode，用get获取login页面
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {"email": email})
        else:
            return render(request, 'active_fail.html')
        return render(request, "login.html")


# 修改密码行为
class ModifyPwdView(View):
    def post(self, request):
        modify_reset = ModifyPwdForm(request.POST)
        if modify_reset.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {"email": email, 'msg': u"密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'login.html')
        else:
            email = request.POST.get("email", "")
            return render(request, 'password_reset.html', {"email": email, " modify_reset": modify_reset})
