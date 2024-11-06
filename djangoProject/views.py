from django.shortcuts import HttpResponse, render
from django.views.decorators.http import require_http_methods


def add_cookie(request):
    response = HttpResponse("添加cookie")
    max_age = 60*60*24*7
    response.set_cookie('username', 'ninuan', max_age=max_age)
    return response

def delete_cookie(request):
    response = HttpResponse("删除cookie")
    response.delete_cookie('username')
    return response

def get_cookie(request):
    username = request.COOKIES.get('username')
    print(username)
    return HttpResponse(username)

def add_session(request):
     request.session['user_id'] = 'ninuan'
     return HttpResponse('添加session')

def get_session(request):
    username = request.session.get('user_id')
    print(username)
    return HttpResponse(username)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print(request.POST)
        print(request.COOKIES)
        return HttpResponse('登录')