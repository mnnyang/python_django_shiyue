# coding=utf-8
import os

from django.contrib.auth import authenticate, login
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from dss.Serializer import serializer

from main.utils import format_to_json, response_json
from users.forms import LoginForm, UserInfoForm


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            print(request.POST, ' ', user_name, ' ', pass_word)

            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                print(user)
                return HttpResponse(format_to_json(1, msg="登录成功！", data=serializer(user)),
                                    content_type='application/ajax')
            else:
                return HttpResponse(format_to_json(2, msg="密码错误！"),
                                    content_type='application/ajax')

        else:
            return HttpResponse(format_to_json(3, msg="数据验证失败！", data=login_form.errors),
                                content_type='application/ajax')


class UserInfo(View):
    def get(self, request):
        print request.COOKIES
        if request.user.is_authenticated():
            return response_json(1, "已登录！", serializer(request.user))
        else:
            return response_json(2, "未登录！")

    def post(self, request):

        if not request.user.is_authenticated():
            return response_json(2, "未登录！")

        # 处理头像文件
        if request.GET.get('type', 0) == '1':
            try:
                img = request.FILES.get('avator')
                f = open(os.path.join('file/upload/avator', img.name), 'wb')
                for chunk in img.chunks(chunk_size=1024):
                    f.write(chunk)

                img_path = os.path.join('upload/avator', img.name)
                print(img_path)
                cursor = connection.cursor()
                cursor.execute("update users_userprofile set avator='{avator}' where id='{id}'".format(
                    avator=img_path, id=request.user.id))
                cursor.close()
                return response_json(1, "修改成功！")
            except BaseException:
                return response_json(2, "修改失败！")

        form = UserInfoForm(request.POST)
        if form.is_valid():
            nick_name = request.POST.get(u"nick_name")
            introduce = request.POST.get(u"introduce")

            cursor = connection.cursor()
            cursor.execute(
                "update users_userprofile set nick_name='{nick_name}',introduce='{introduce}' where id='{id}'".format(
                    nick_name=nick_name, introduce=introduce, id=request.user.id))
            cursor.close()
            return response_json(1, "修改成功！")
        else:
            return response_json(3, "验证失败！")
