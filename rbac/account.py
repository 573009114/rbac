from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from rbac.models import *
from rbac import form
from rbac import query

import hashlib,time

def login(req):
    ''' 用户登录 '''
    if req.method == 'POST':
        forms = form.UserForm(req.POST)
        if forms.is_valid():
            username=forms.cleaned_data['username']
            passwd=forms.cleaned_data['password']
            sign = hashlib.sha1()
            sign.update(passwd.encode('utf8'))
            password = sign.hexdigest()
            auth = User.objects.filter(username__exact = username,password__exact = password)
            if auth:
                last_login=User.objects.filter(username=username).update(last_login=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                response=HttpResponseRedirect('/')
                response.set_cookie('username',username,3600)
                return response
            else:
                return render(req,'backend/login.html',{"msg":"用户名不存在，或者密码错误！"})
    else:
        forms = form.UserForm(req.POST)
        
    kwargs = {
        'form': form,
    }
    return render(req, 'backend/login.html', kwargs)

def register(req):
    '''注册用户 '''
    msg=''
    mid='0'  # 超级权限置为0
    rid='0'  
    model=query.ResultID.model_info(mid)
    role=query.ResultID.role_info(rid)
    if req.method == 'POST':
        forms = form.RegisterForm(req.POST)
        if forms.is_valid():
            username=req.POST.get('username')
            active=req.POST.get('is_active','1')
            email=req.POST.get('email')
            rid=req.POST.get('rid')
            _result=User.objects.filter(username=username)
            if _result:
                msg='用户名已存在'
            else:
                password1=req.POST.get('password1')
                password2=req.POST.get('password2')
                sign1=hashlib.sha1()
                sign1.update(password1.encode('utf8'))
                password1=sign1.hexdigest()
                sign2=hashlib.sha1()
                sign2.update(password2.encode('utf8'))
                password2=sign2.hexdigest()
                if (password2 != password1 ): 
                    msg='两次密码不一致'
                    return HttpResponse('<script type="text/javascript">alert("%s");location.href="javascript:history.back(-1);"</script>'% msg)
                else:
                    password=password2
                    uid=query.ResultID.create_user(username,password1,active,email)
                    query.ResultID.update_user_role(uid,rid)
                    msg='注册成功'
                    return HttpResponse('<script type="text/javascript">alert("%s");location.href="javascript:history.back(-1);"</script>'% msg)
        else:
            forms=form.RegisterForm(req.POST)
    kwargs = {
        'form':form,
        'msg':msg,
        'role':role, 
        'model':model,
    }
    return render(req,'backend/user-register.html', kwargs)

def logout(req):
    body='aa'
    response=HttpResponse(body)
    #清除cookie里保存的username
    response.delete_cookie('username')
    return response
