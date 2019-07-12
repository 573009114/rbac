#coding:utf-8
from django.shortcuts import render,render_to_response
from rbac.models import *

def renders(req):
    model=Model.objects.all().values('model_name','model_url')
    context={
        'model':model,
        }
#    return context
#    print(model)
    return model
