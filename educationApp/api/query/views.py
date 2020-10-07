from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def query_page(request):
    return HttpResponse('<h1>Query Page</h1>')