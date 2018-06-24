from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'type/(?P<type_good>.*)/', views.index)
]