from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """dj_projects Home"""
    return render(request, 'dj_projects/index.html')


def topics(request):
    """
    Show all topics
    URL: http://localhost:8000/topics/
    """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'dj_projects/topics.html', context)
