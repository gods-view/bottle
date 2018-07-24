from django.contrib import admin
from user.models import Passport


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键
    list_display = ('username', 'password', 'email')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 30

    # # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('-create_time',)

    # list_editable 设置默认可编辑字段
    # list_editable = ['machine_room_id', 'temperature']

    # 筛选器
    list_filter = ('username', 'email')  # 过滤器
    search_fields = ('username', 'email')  # 搜索字段


class MyAdminSite(admin.AdminSite):
    site_header = 'bottle后台管理'  # 此处设置页面显示标题
    site_title = 'bottle运维'  # 此处设置页面头部标题


admin_site = MyAdminSite(name='management')

admin.site.register(Passport, UserAdmin)
