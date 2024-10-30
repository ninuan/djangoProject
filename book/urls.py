from django.urls import path
from . import views

app_name = 'book'

urlpatterns = {
    path('sql', views.index, name='index'),
    path('add', views.add_book, name='add_book'),
    path('query', views.query_book, name='query_book'),
}