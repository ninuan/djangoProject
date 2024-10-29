from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def movie_list(request):
    return HttpResponse('Movie List')

def movie_detail(request, movie_id):
    return HttpResponse(f'Movie Detail: {movie_id}')

def index(request):
    return render(request, 'index.html')

def info(request):
    username = 'admin'
    # 2. 字典类型
    book = {'name': '水浒传', 'author': '施耐庵'}
    # 3. 列表
    books = [
        {'name': '水浒传', 'author': '施耐庵'},
        {'name': '三国演义', 'author': '罗贯中'},
    ]
    # 4. 对象
    class Person:
        def __init__(self, realname):
            self.realname = realname
    context = {
        'username': username,
        'book': book,
        'books': books,
        'person': Person('admin')
    }
    return render(request,'info.html',context=context)

def if_view(request):
    age = 17
    return render(request, 'if.html', context={'age': age})

def for_view(request):
    # 1. 列表
    books = [
        {'name': '水浒传', 'author': '施耐庵'},
        {'name': '三国演义', 'author': '罗贯中'},
    ]
    # 2. 字典
    person={
        'realname': 'admin',
        'age': 17,
        'height': 180
    }
    context = {
        'books': books,
        'person': person
    }
    return render(request, 'for.html', context=context)

def with_view(request):
    context = {
        'books': [
            {'name': '水浒传', 'author': '施耐庵'},
            {'name': '三国演义', 'author': '罗贯中'},
        ]
    }
    return render(request, 'with.html', context=context)

def url_view(request):
    return render(request, 'url.html')