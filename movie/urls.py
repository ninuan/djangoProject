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
    path('for', views.for_view, name='for'),
    path('with', views.with_view, name='with'),
    path('url', views.url_view, name='url'),
    path('filter', views.filter_view, name='filter',),
    path('template/form', views.template_form, name='template_form'),
]