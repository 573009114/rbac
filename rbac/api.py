from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.



class api_v1:
    
     def index(req):
         return HttpResponse('index')
     
     def user_info(req):
         
         return render(req,'backend/admin-edit.html')
     
     
     def role(req,id):
         return render(req,'backend/admin-rule.html')
     
     def menu(req):
         return render(req,'backend/admin-rule.html')
     
     def permission_group(req,id):
         return HttpResponse('permission_group')
     
     def permission_rule(req,id):
         return HttpResponse('permission_rule')
     
