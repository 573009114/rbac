from django.db import models

# Create your models here.
class Model(models.Model):
    model_name=models.CharField('菜单名称',max_length=32)
    model_code=models.CharField('菜单code',max_length=32,unique=True)
    model_url=models.CharField('菜单url',max_length=32)
    class Meta:
        verbose_name_plural = "菜单表"

class User(models.Model):
    username = models.CharField('用户名',max_length=32,unique=True)
    password = models.CharField('密码',max_length=64)
    email = models.CharField('邮箱',max_length=32)
    mobile = models.CharField('电话',max_length=11)
    is_active = models.BooleanField(default=1)
    create_datetime=models.DateTimeField('创建时间',auto_now = True)
    update_dateimte=models.DateTimeField('更新时间',auto_now_add = True)
    last_login=models.DateTimeField('最后登录日期', blank=True,null=True)
    roles=models.ManyToManyField(verbose_name='角色',to="Role")
    def __str__(self):
        return  self.username

class Role(models.Model):
    role_name=models.CharField('角色名称',max_length=32)
    role_describe=models.CharField('角色描述',max_length=64)
    model=models.ManyToManyField(verbose_name='规则表',to="Model")
    class Meta:
        verbose_name_plural = "角色表"
