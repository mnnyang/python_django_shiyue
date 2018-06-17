from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class UserInfoForm(forms.Form):
    nick_name = forms.CharField(required=True, min_length=3, max_length=50)
    introduce = forms.CharField(required=True, max_length=1000)
    # avator = forms.CharField(required=True, max_length=100)
