from django.db import models


# Create your models here.


class Department(models.Model):
    """部门表"""
    department_name = models.CharField(max_length=64, verbose_name='部门名称')


class UserInfo(models.Model):
    """用户表"""
    user_name = models.CharField(max_length=32, verbose_name="用户登录名")
    user_pwd = models.CharField(max_length=64, verbose_name="用户密码")
    # 创建帐号状态元组
    state_choices = (
        (1, "启用"),
        (2, "禁用"),
    )
    user_state = models.SmallIntegerField(verbose_name="帐号状态", choices=state_choices)


