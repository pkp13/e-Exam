from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_page),
    path('category/', include('api.category.urls')),
    path('questions/', include('api.questions.urls')),
    path('featured_art/', include('api.featured_art.urls')),
    path('queries/', include('api.query.urls')),
    path('user/', include('api.user.urls')),
    path('test/', include('api.basic_test.urls')),
]
