from tkinter.font import names

from django.urls import path
from . import views

# 指定应用名称（应用命名空间）
app_name = 'movie'

urlpatterns = [
    path('', views.index),
    path('info', views.info, name='info'),
    path('list', views.movie_list, name='movie_list'),
    path('detail/<int:movie_id>', views.movie_detail, name='index'),
    path('if', views.if_view, name='if'),
]