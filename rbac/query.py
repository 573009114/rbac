from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Count
from rbac.models import *
import time

class ResultID:
    ''' 返回查询数据  '''    
    def role_info(rid):
        if rid =='0':
            role_list=Role.objects.all().values('id','role_name','role_describe')
            total=Role.objects.aggregate(Count('id'))
        else:
            role_list=Role.objects.filter(id=rid).values('id','role_name','role_describe')
            total=1

        result={
            'role_list':role_list,
            'total':total,
        }
        return result

    def model_info(mid):
        if mid == '0':
            model_list=Model.objects.all().values('id','model_name','model_code','model_url')
            total=Model.objects.aggregate(Count('id'))
        else:
             model_list=Model.objects.filter(id=mid).values('id','model_name','model_code','model_url')
             total=1

        result={
            'model_list':model_list,
            'total':total,
        }
        return result

    def user_info(uid):
        if uid == '0':
            userlist=User.objects.all().values('id','username','email','mobile','is_active','create_datetime','update_dateimte','last_login','roles__id','roles__role_name')
            total=User.objects.aggregate(Count('id'))
        else:
            userlist=User.objects.filter(id=uid).values('id','username','email','mobile','is_active','create_datetime','update_dateimte','last_login','roles__id','roles__role_name')
            total=1

        result={
            'ul':userlist,
            'total':total, 
        }
        return result


    '''创建记录操作'''

    def create_model(mname,mtoken,murl):
        create_model=Model.objects.create(model_name=mname,model_code=mtoken,model_url=murl)
        create_model.save()
        return create_model.id

    def create_user(username,password1,active,email):
        timer=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(timer)
        create_user = User.objects.create(username=username,password=password1,is_active=active,email=email,create_datetime=timer)
        create_user.save()
        return create_user.id

    def create_role(rolename,describe):
        create_role=Role.objects.create(role_name=rolename,role_describe=describe)
        create_role.save()
        return create_role.id


    '''更新表操作'''
    def update_user_role(uid,rid):
        obj=User.objects.filter(id=uid).first()
        obj.roles.add(rid)
        return obj

    def update_role_model(rid,mid):
        obj=Role.objects.filter(id=rid).first()
        obj.model.add(*mid)
        return obj
 
    ''' 删除记录操作 '''
    def delete_user(uid):
        if uid:
            User.objects.filter(id=uid).delete()
            msg='记录删除完成'
        else:
            msg='记录删除失败'
        return msg

    def delete_role(rid):
        if rid:
            Role.objects.filter(id=rid).delete()
            msg='记录删除完成'
        else:
            msg='记录删除失败'
        return msg

    def delete_model(mid):
        if mid:
            Model.objects.filter(id=mid).delete()
            msg='记录删除完成'
        else:
            msg='记录删除失败'
        return msg

    ''' 修改记录 '''
    def edit_model(mid,model_name,model_url):
        update_model=Model.objects.filter(id=mid).update(model_name=model_name,model_url=model_url)
        msg="修改完成"
        return msg

    def edit_role(rid,role_name,role_describe,mid):
        update_role=Role.objects.filter(id=rid).update(role_name=role_name,role_describe=role_describe)
        obj=Role.objects.filter(id=rid).first()
        obj.model.set(mid)
        msg="修改完成"
        return msg

    def edit_user(uid,mobile,email,rid):
        timer=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        update_user=User.objects.filter(id=uid).update(mobile=mobile,email=email,update_dateimte=timer)
        obj=User.objects.filter(id=uid).first()
        obj.roles.set(rid)
        msg='修改完成'
        return msg
