from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Topics,Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request, 'learning_log_app/home.html')
@login_required
def topics(request):
    topics = Topics.objects.filter(owner = request.user).order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'learning_log_app/topics.html', context)
@login_required
def topic(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('date_added')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'learning_log_app/topic.html', context)
@login_required
def addTopic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid:
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_log_app:topics'))
    context = {'form' : form}
    return render(request, 'learning_log_app/addTopic.html', context)
@login_required
def deleteTopic(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    topic.delete()
    return HttpResponseRedirect(reverse('learning_log_app:topics'))
@login_required
def addEntry(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_log_app:topic', args=[topic_id]))
    context = {'topic': topic, 'form' : form}
    return render(request, 'learning_log_app/addEntry.html', context)
@login_required
def editEntry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_log_app:topic', args=[topic.id]))
    context = {'form' : form, 'topic' : topic, 'entry' : entry}
    return render(request, 'learning_log_app/editEntry.html', context)
@login_required
def deleteEntry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    entry.delete()
    return HttpResponseRedirect(reverse('learning_log_app:topic', args=[topic.id]))
