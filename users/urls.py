"""Define URL patterns for users App"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Include default auth urls, provided by Django
    # This Django default URLs includes 'login' & 'logout' and so on
    path('', include('django.contrib.auth.urls')),
]