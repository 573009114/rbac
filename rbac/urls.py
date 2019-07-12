"""AuthenticationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path

from rbac import (index,account,views)

urlpatterns = [
    path('',index.index,name='home'),
    path('login',account.login,name='login'),
    path('logout',account.logout,name='logout'),
    re_path('members/user/(\d+)/',views.user_info,name='user'),
    path('members/user/add',account.register,name='user_add'),
    path('members/user/delete',views.user_del,name='user_delete'),
    path('members/user/edit',views.user_edit,name='user_delete'),
    re_path('members/role/(\d+)/',views.role_info,name='role'),
    path('members/role/add',views.role_create,name='role_add'),
    path('members/role/delete',views.role_del,name='role_del'),
    path('members/role/edit',views.role_edit,name='role_del'),
    re_path('members/model/(\d+)/',views.model_info,name='model'),
    path('members/model/add',views.model_create,name='model_add'),
    path('members/model/delete',views.model_del,name='model_del'),
    path('members/model/edit',views.model_edit,name='model_del'),
]
