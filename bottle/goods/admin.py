from django.contrib import admin
from goods.models import Products
from django.utils.safestring import mark_safe
from django.db import models
from django.utils.safestring import mark_safe


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键
    def image_data(self, obj):
        if obj.image:
            return mark_safe(obj.image.url)
        else:
            return '(no image)'

    def imgurl_data(self, obj):
        return obj.image.url

    # 页面显示的字段名称
    image_data.short_description = u'类别图片'
    list_display = ('category', 'title', 'subhead', 'description', 'image_data', 'imgurl')
    readonly_fields = ('image_data',)

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 30

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-update_time',)

    # list_editable 设置默认可编辑字段
    # list_editable = ['machine_room_id', 'temperature']

    # 筛选器
    list_filter = ('category',)  # 过滤器
    search_fields = ('category',)  # 搜索字段
    date_hierarchy = 'create_time'  # 详细时间分层筛选


admin.site.register(Products, ProductAdmin)
