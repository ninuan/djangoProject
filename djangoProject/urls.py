"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from book import views
from django.urls import include
from django.urls import reverse
from . import views as vi


def index(request):
    print(reverse('movie:index',kwargs={'movie_id':1}))
    return HttpResponse("Hello, World!")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("book", views.book_detail_query_string, name='book_detail_query_string'),
    # http://127.0.0.1/book/1
    # 在book_id前面指定参数类型有两个好处：
    # 1. 可以限制参数类型，如果传入的参数类型不符合要求，Django会返回404错误
    # 2. 在视图函数当中得到的就是一个整形，否则默认是str类型
    path('book/<int:book_id>',views.book_detail_path),
    path('movie/', include("movie.urls")),
    path('book/', include("book.urls")),
    path('article/', include('article.urls')),
    path('front/', include('front.urls')),
    path('front_1/', include('front_1.urls')),
    path('cookie/add', vi.add_cookie, name='add_cookie'),
    path('cookie/delete', vi.delete_cookie, name='delete_cookie'),
    path('cookie/get', vi.get_cookie, name='get_cookie'),
    path('session/add', vi.add_session, name='add_session'),
    path('session/get', vi.get_session, name='get_session'),
    path('login/', vi.login, name='login'),
] + static(settings.MEDIA_URL,documnet_root=settings.MEDIA_ROOT)
