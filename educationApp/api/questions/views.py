from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def question_page(request):
    return HttpResponse("<h1>Questions Page</h1>")