from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Section, Topic, Tag, Resource, Fail, Question, Practice, Strategy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import SectionForm, TopicForm


# Create your views here.
# @login_required(login_url='/login/') #TODO: add back in
def dashboard(request):
    context = {
        'user': User.objects.first()
    }
    return render(request, 'make_charts/dashboard.html', context)


# @login_required(login_url='/login/') #TODO: add back in
# def add_questions(request):
#     context = {
#         'user': User.objects.first()
#     }
#     return render(request, 'make_charts/practice_questions.html', context)


# @login_required(login_url='/login/') #TODO: add back in
def add_practice(request):
    context = {
        'user': User.objects.first()
    }
    return render(request, 'make_charts/practice_questions.html', context)


# @login_required(login_url='/login/') #TODO: add back in
def add_section(request):
    sec_form = SectionForm()
    topic_form = TopicForm()
    if request.method == 'POST':
        bound_form = SectionForm(request.POST)
        print(bound_form)
        if bound_form.is_valid():
            this_user = User.objects.last() #TODO: make this the user in session!!!!!!!!
            Section.objects.create(title=request.POST['section_title'], user=this_user)
        context = {
            'sections': Section.objects.all(),
            'secForm': sec_form,
            'topicForm': topic_form 
        }
        return render(request, 'make_charts/section_topics_tags.html', context)
    context = { 
            'sections': Section.objects.all(),
            'secForm': sec_form,
            'topicForm': topic_form 
        }
    return render(request, 'make_charts/section_topics_tags.html', context)


# def create_section(request):
#     payload = {'success': True}
#     print("hey line 44")
#     return JsonResponse(payload)


# def create_section(request):
    