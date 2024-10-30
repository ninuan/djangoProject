from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from book.models import Book


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
    book = Book(name="三国演义", author="罗贯中", price=99.9)
    book.save()
    return HttpResponse("添加成功")

def query_book(request):
    books = Book.objects.all()
    for book in books:
        print(book.id, book.name, book.author, book.pub_time, book.price)
    return HttpResponse("查询成功")
