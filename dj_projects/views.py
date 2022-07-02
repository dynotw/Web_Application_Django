from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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

# Views function for Page which adds new topic not in admin page
def new_topic(request):
    """Add a new topic"""
    if request.method != "POST":
        # No data submitted, then create a blank form
        form = TopicForm()
    else:
        # POST data submitted , then process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dj_projects:topics')
    context = {'form': form}
    return render(request, 'dj_projects/new_topic.html', context)

# Views function for Page which adds new entry for topic_id
def new_entry(request, topic_id):
    """Add a new entry for a topic with topic_id"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        """No data submitted, then create a blank"""
        form = EntryForm()
    else:
        # POST data submitted, then process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            print("Hello")
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('dj_projects:topic', topic_id=topic_id)
    # No data submitted or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'dj_projects/new_entry.html', context)

# Views function for editing entry with entry_id
def edit_entry(request, entry_id):
    """Edit an existed entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != "POST":
        # Initial request, pre-fill form with the current entry
        form = EntryForm(instance=entry, data=request.POST)
    else:
        # POST data submitted, then process data
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dj_projects:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'dj_projects/edit_entry.html', context)