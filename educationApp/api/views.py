from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def api_page(request):
    return HttpResponse("<h1>API PAGE</h1>")
    