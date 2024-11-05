from django.db.models.expressions import result
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Publisher, Author, BookOrder
from django.db.models import Avg, Count, Max, Min, Sum, F, Q

# Create your views here.
def avg_view(request):
    result = Book.objects.aggregate(Avg('price'))
    print(result)
    return HttpResponse("Avg view")

def count_view(request):
    result = Book.objects.aggregate(Count('id'))
    print(result)
    return HttpResponse("Count view")

def max_min_view(request):
    result = Author.objects.aggregate(Max('age'), Min('age'))
    print(result)
    return HttpResponse("Max Min view")

def sum_view(request):
    result = Book.objects.annotate(total=Sum('bookorder__price')).values('name','total')
    print(result)
    return HttpResponse("Sum view")

def f_view(request):
    Book.objects.update(price=F('price')-10)
    return HttpResponse("F view")

def q_view(request):
    books = Book.objects.filter(Q(price__gte=80) | Q(rating__gte=9))
    for book in books:
        print(book.name, book.price, book.rating)
    return HttpResponse("Q view")