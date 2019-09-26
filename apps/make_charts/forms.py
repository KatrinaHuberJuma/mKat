from django import forms
from .models import Section, Topic, Tag, Resource, Fail, Question, Practice, Strategy


class SectionForm(forms.Form):
    section_title = forms.CharField(max_length=45)
    

class TopicForm(forms.Form):
    topic_title = forms.CharField(max_length=45)
    section = forms.ModelChoiceField(queryset=Section.objects.all())
#     # todo: further study 
#     confidence = models.IntegerField()
#     # linked to Question by related_name="questions")
#     # related to Tag, related name="tags"
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)