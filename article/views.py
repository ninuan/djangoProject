from django.http import HttpResponse
from django.shortcuts import render
from .models import User,Article

# Create your views here.
def article_test(request):
    # user = User(username='admin',password='123456')
    # user.save()
    # article = Article(title='Chat发布', content='xxx', author=user)
    # article.save()

    article = Article.objects.first()
    return HttpResponse(article.author.username)

def one_to_many(request):
    user = User.objects.first()
    articles = user.articles.filter(title__contains='Chat').all()
    for article in articles:
        print(article.title)
    return HttpResponse("查询成功")

def query1(request):
    # article = Article.objects.filter(id__exact=1)
    # article = Article.objects.filter(title__iexact='chat发布')
    article = Article.objects.filter(title__contains='Chat')
    print(article.query)
    print(article)
    return HttpResponse("查询成功")