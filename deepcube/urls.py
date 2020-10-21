from django.views.generic import RedirectView
from django.conf.urls import url
from django.urls import path
from . import views             # 从views.py导入所有页面调用有关的函数

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', RedirectView.as_view(url='index/')),
    path('index/initState/', views.initState, name='initState'),
    path('index/solve/', views.solve, name='solve'),
]