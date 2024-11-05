from django.http import HttpResponse
from django.shortcuts import render
from .forms import MessageBoardForm, RegisterForm, ArticleForm
# 请求验证装饰器
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        form = MessageBoardForm()
        return render(request, 'index.html', context={'form': form})
    else:
        # 对用post请求提交上来的数据，用表单验证是否满足要求
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            return HttpResponse(f"{title}, {content}, {email}")
        else:
            print(form.errors)
            return HttpResponse("表单验证失败")

@require_http_methods(['GET', 'POST'])
def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            return HttpResponse(f"{telephone}")
        else:
            print(form.errors)
            return HttpResponse("表单验证失败")

@require_http_methods(['GET', 'POST'])
def article_view(request):
    if request.method == 'GET':
        return render(request, 'article.html')
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            return HttpResponse(f"{title}, {content}")
        else:
            print(form.errors)
            return HttpResponse("表单验证失败")