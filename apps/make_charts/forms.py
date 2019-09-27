from django import forms
from .models import Section, Topic, Tag, Resource, Fail, Question, Practice, Strategy



class SectionForm(forms.Form):
    section_title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'title'}))
    


class TopicForm(forms.Form):
    topic_title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'title'}))
    # section = forms.ModelChoiceField(queryset=Section.objects.all(), empty_label=None)
    # ??? Why can't I get the ModelChoiceField (above) to display the title instead of "Section Object"???

class TagForm(forms.Form):
    tag_title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'title'}))
    