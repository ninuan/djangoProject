from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from book.models import Book
from .models import Tag


# Create your views here.
def book_detail_query_string(request):
    book_id = request.GET.get("id")
    name = request.GET.get("name")
    return HttpResponse(f"Book ID: {book_id}, Book Name: {name}")

def book_detail_path(request, book_id):
    return HttpResponse(f"Book ID: {book_id}")

def index(request):
    cursor = connection.cursor()
    cursor.execute("select * from book")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return HttpResponse("chaxun")

def add_book(request):
    book = Book(name="三国演义", author="罗贯中", price=99)
    book.save()
    return HttpResponse("添加成功")

def query_book(request):
    books = Book.objects.filter(name='三国演义')
    for book in books:
        print(book.id, book.name, book.author, book.pub_time, book.price)
    return HttpResponse("查询成功")

def order_view(request):
    # books = Book.objects.order_by("pub_time")
    books = Book.objects.all()
    for book in books:
        print(book.name, book.pub_time)
    return HttpResponse("排序成功")

def update_view(request):
    book = Book.objects.first()
    book.name = '红楼梦'
    book.save()
    return HttpResponse("修改成功")

def delete_view(request):
    book = Book.objects.filter(name='红楼梦')
    book.delete()
    return HttpResponse("删除成功")

def book_tag(request):
    tag = Tag()
    tag.save()
    return HttpResponse("Tag插入成功")
