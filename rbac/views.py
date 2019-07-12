from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from rbac.models import *
from django.db.models import Count
from django.template import RequestContext
from rbac import query,utils
import random
import string
from rbac.required import check_login
from rbac import initial

# 查看显示部分

@check_login
def user_info(req,uid):
    ''' 用户信息 '''
    userinfo=query.ResultID.user_info(uid)
    context_instance=utils.renders(req)
    models_info=initial.init_role(uid)
    request_url = req.path_info
    print(models_info)
    if 'user' in request_url:
        print(models_info)
    return render_to_response('backend/user-list.html',locals())
#    return render_to_response('backend/user-list.html')


@check_login
def role_info(req,rid):
    ''' 角色信息 '''
    if rid =='0':
        role_list=Role.objects.all().values('id','role_name','role_describe','model__model_name')
        total=Role.objects.aggregate(Count('id'))
    else:
        role_list=Role.objects.filter(id=rid).values('id','role_name','role_describe','model__model_name')
        total=1

    kwargs={
        'role_list':role_list,
        'total':total,
        'context_instance':utils.renders(req),
    }
    
    return render_to_response('backend/role-list.html',kwargs)

@check_login
def model_info(req,mid):
    ''' 菜单信息 '''
    modelinfo=query.ResultID.model_info(mid)
    context_instance=utils.renders(req)
    return render_to_response('backend/model-list.html',locals())


# 删除部分
def user_del(req):
    ''' 删除用户 '''
    uid=req.GET.get('id')
    msg=query.ResultID.delete_user(uid)
    return HttpResponse('<script type="text/javascript">alert("%s");location.href="javascript:history.back(-1);"</script>'% msg)

def role_del(req):
    rid=req.GET.get('id')
    msg=query.ResultID.delete_role(rid)
    return HttpResponse('<script type="text/javascript">alert("%s");location.href="javascript:history.back(-1);"</script>'% msg)

def model_del(req):
    mid=req.GET.get('id')
    msg=query.ResultID.delete_model(mid)
    return HttpResponse('<script type="text/javascript">alert("%s");location.href="javascript:history.back(-1);"</script>'% msg)


# 创建部分
def role_create(req):
    ''' 创建角色 '''

    mid = '0'   #mid置为0，表示超级管理员权限

    modelinfo=query.ResultID.model_info(mid)
    if req.method == 'POST':
        rolename=req.POST.get('rolename')
        describe=req.POST.get('desc')
        mid=req.POST.getlist('modelid[]')
        rid=query.ResultID.create_role(rolename,describe)
        query.ResultID.update_role_model(rid,mid)
        msg='创建成功'
        return HttpResponse('<script type="text/javascript">alert("%s");location.href="javascript:history.back(-1);"</script>'% msg)     
    return render(req,'backend/role-add.html',{'modelinfo':modelinfo})


def model_create(req):
    ''' 创建菜单 '''
    if req.method == "POST":
        mname=req.POST.get('model_name')
        murl=req.POST.get('model_url')
        mtoken=''.join(random.sample(string.digits, 6))
        query.ResultID.create_model(mname,mtoken,murl)
        msg="创建成功"
        return HttpResponse('<script type="text/javascript">alert("%s");location.href="javascript:history.back(-1);"</script>'% msg)

    return render(req,'backend/model-add.html')


# 修改部分
def model_edit(req):
    mid=req.GET.get('id')
    if mid:
        models=query.ResultID.model_info(mid)
        if req.method == 'POST':
            model_name=req.POST.get('modelname')
            model_url=req.POST.get('modelurl') 
            msg=query.ResultID.edit_model(mid,model_name,model_url)
            return HttpResponse('<script type="text/javascript">alert("%s");location.href="javascript:history.back(-1);"</script>'% msg)
    kwargs={
        'models':models,
    }
    return render(req,'backend/model-edit.html',kwargs)

def role_edit(req):
    rid=req.GET.get('id')
    modelinfo=query.ResultID.model_info(mid='0')
    if rid:
        roles=query.ResultID.role_info(rid)
        if req.method == 'POST':
            role_name=req.POST.get('rolename')
            role_describe=req.POST.get('desc')
            mid=req.POST.getlist('mid[]')
            msg=query.ResultID.edit_role(rid,role_name,role_describe,mid)
            return HttpResponse('<script type="text/javascript">alert("%s");location.href="javascript:history.back(-1);"</script>'% msg)

    kwargs={
        'roles':roles,
        'models':modelinfo,
    }
    return render(req,'backend/role-edit.html',kwargs)

def user_edit(req):
    uid=req.GET.get('id')
    rid='0' #超级权限置为0
    roles=query.ResultID.role_info(rid)
    if uid:
        userinfo=query.ResultID.user_info(uid)
        if req.method == 'POST':
            mobile=req.POST.get('mobile')
            email=req.POST.get('email')
            rid=req.POST.get('rid')
            msg=query.ResultID.edit_user(uid,mobile,email,rid)
            return HttpResponse('<script type="text/javascript">alert("%s");location.href="javascript:history.back(-1);"</script>'% msg)
    kwargs={
        'userinfo':userinfo,
        'roles':roles,
    }
    return render(req,'backend/user-edit.html',kwargs)
