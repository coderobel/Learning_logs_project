from django import forms
from .models import Topics, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['text']
        label = {'text' : ''}
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        label = {'text' : ''}
