from django.urls import path
from . import views

app_name = 'book'

urlpatterns = {
    path('sql', views.index, name='index'),
    path('add', views.add_book, name='add_book'),
    path('query', views.query_book, name='query_book'),
    path('order', views.order_view, name='order_view'),
    path('update', views.update_view, name='update_view'),
    path('delete', views.delete_view, name='delete_view'),
    path('tag', views.book_tag, name='book_tag')
}