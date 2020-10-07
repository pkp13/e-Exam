from django.urls import path
from . import views

urlpatterns = [
    path('', views.featured_art_page),
]
