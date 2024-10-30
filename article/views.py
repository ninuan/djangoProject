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