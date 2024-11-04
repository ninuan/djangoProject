from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Publisher, Author, BookOrder
from django.db.models import Avg, Count, Max, Min

# Create your views here.
def avg_view(request):
    result = Book.objects.aggregate(Avg('price'))
    print(result)
    return HttpResponse("Avg view")

def count_view(request):
    result = Book.objects.aggregate(Count('id'))
    print(result)
    return HttpResponse("Count view")

