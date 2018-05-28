from django.db import models
from django.contrib import admin

# Create your models here.

from django.db import models
from db.base_model import BaseModel  # 导入抽象模型类
from db.base_manager import BaseManager  # 导入抽象模型管理器基类


# Create your models here.


class PassportManager(BaseManager):
    '''账户模型管理器类'''

    def add_one_passport(self, username, password, email):
        '''添加一个注册用户信息'''
        obj = self.create_one_object(username=username, password=password, email=email)
        # 返回对象
        return obj

    def get_one_passport(self, username, password=None):
        '''查找账户信息'''
        if password is None:
            # 根据用户名查找账户信息
            obj = self.get_one_object(username=username)
        else:
            # 根据用户名和密码查找账户信息
            obj = self.get_one_object(username=username, password=password)
        return obj


class Passport(BaseModel):
    '''账户模型类'''
    username = models.CharField(max_length=20, verbose_name='账户名称')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')

    objects = PassportManager()  # 自定义模型管理器类对象

    class Meta:
        db_table = 'user'

