from django.urls import path
from . import views

urlpatterns = [
    path('avg', views.avg_view, name='avg_view'),
    path('count', views.count_view, name='count_view'),
]