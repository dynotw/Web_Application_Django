from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """dj_projects Home"""
    return render(request, 'dj_projects/index.html')

# views function that Show all topics
def topics(request):
    """
    Show all topics
    URL: http://localhost:8000/topics/
    """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'dj_projects/topics.html', context)

# Views function that show an individual topic, based on topic_id
def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added') # '-' this minus sign means reverse order
    context = {'topic': topic, 'entries': entries}
    return render(request, 'dj_projects/topic.html', context)

