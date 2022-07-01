"""
Define dj_projects URL mode
"""

from django.urls import path
from . import views

# This app_name helps Django distinguish urls.py from others from other App
app_name = 'dj_projects'
# This urlpatterns is a list of URL which can be requested from dj_projects App
urlpatterns = [
    # Home
    # 1.URL; 2.View function (from views.py); 3.Template (index.html)
    path('', views.index, name='index'),
    # Page which shows all topics
    path('topics/', views.topics, name='topics'),
    # Page which shows an individual topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]

