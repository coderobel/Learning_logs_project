from django.urls import path
from . import views
app_name = 'learning_log_app'

urlpatterns = [
    path('' , views.home, name='home' ),
    path('topics/', views.topics, name='topics'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('deleteTopic/<int:topic_id>', views.deleteTopic, name='deleteTopic'),
    path('addTopic/', views.addTopic, name='addTopic'),
    path('addEntry/<int:topic_id>', views.addEntry, name='addEntry'),
    path('editEntry/<int:entry_id>', views.editEntry, name='editEntry'),
    path('deleteEntry/<int:entry_id>', views.deleteEntry, name='deleteEntry'),
]