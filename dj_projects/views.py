from django.shortcuts import render

# Create your views here.
def index(request):
    """dj_projects Home"""
    return render(request, 'dj_projects/index.html')