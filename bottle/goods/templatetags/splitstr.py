from django import template
import time
import datetime

# 创建模板库的实例
register = template.Library()


# 注册过滤器
@register.filter
def splitstr(temp_str):
    result = temp_str.split(",")
    return result
