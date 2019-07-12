#coding=utf-8

from django import forms
from rbac.models import *

class UserForm(forms.Form): 
    ''' 用户登录  '''
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    ''' 用户注册 '''
    username = forms.CharField(label='用户名')
    email = forms.EmailField(
        required=True,
        error_messages={'required': "邮箱不能为空", 'invalid': "邮箱格式错误"},
        widget=forms.EmailInput()
    )
    password1 = forms.CharField(
        label='密码',
        error_messages={'required': "密码不能为空"},
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='重复密码',
        error_messages={'required': "密码不能为空"},
        widget=forms.PasswordInput()
    )

