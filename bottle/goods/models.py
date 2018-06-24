from django.db import models
from db.base_model import BaseModel  # 导入抽象模型类
from db.base_manager import BaseManager  # 导入抽象模型管理器基类
from django.utils.safestring import mark_safe
from DjangoUeditor.models import UEditorField


class ProductsManager(BaseManager):
    '''账户模型管理器类'''

    def get_one_passport(self, category):
        '''查找账户信息'''
        # 根据用户名查找账户信息
        obj = self.get_one_object(category=category)
        return obj


# Create your models here.
class Products(BaseModel):
    category = models.CharField(max_length=20, verbose_name="产品类别")
    title = models.CharField(max_length=50, verbose_name="标题")
    subhead = models.CharField(max_length=100, verbose_name="副标题")
    description = models.TextField(verbose_name="描述")
    image = models.ImageField(u'图片', upload_to='img/goods', null=True)
    Content = UEditorField(u'内容', width=600, height=300, toolbars="full", imagePath="img/goods", filePath="",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, command=None, event_handler=None, blank=True)
    imgurl = models.CharField(max_length=100, default="", verbose_name="图片地址")

    def image_data(self, obj):
        return obj.image.url

    # 页面显示的字段名称
    image_data.short_description = u'类别图片'

    objects = ProductsManager()  # 自定义模型管理器类对象

    class Meta:
        db_table = 'products'
