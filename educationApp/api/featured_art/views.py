from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def featured_art_page(request):
    # return HttpResponse("<h1>Featured Art Page</h1>")
    return render(request, 'featuredArt.html')