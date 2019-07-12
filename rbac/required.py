#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from rbac.models import *


#登录装饰器
def check_login(func):
  def _check_login(req,*args,**kwargs):
    username=req.COOKIES.get('username')
    if not username:
      return HttpResponseRedirect('/login')
    return func(req,*args,**kwargs)
  return _check_login

