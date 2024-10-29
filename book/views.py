from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def book_detail_query_string(request):
    book_id = request.GET.get("id")
    name = request.GET.get("name")
    return HttpResponse(f"Book ID: {book_id}, Book Name: {name}")

def book_detail_path(request, book_id):
    return HttpResponse(f"Book ID: {book_id}")