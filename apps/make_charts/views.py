from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Section, Topic, Tag, Resource, Fail, Question, Practice, Strategy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import SectionForm, TopicForm, TagForm


# Create your views here.
# @login_required(login_url='/login/') #TODO: add back in
def dashboard(request):
    context = {
        'user': User.objects.first()
    }
    return render(request, 'make_charts/dashboard.html', context)

def pie_chart(request):
    fails = Fail.objects.exclude(title="N/A")
    questions = Question.objects.filter(answered_correctly=False)
    questions_by_fail ={ }
    # print(questions)
    # print(fails)
    for f in fails:
        questions_by_fail[f.id] = {'title': f.title, "victims": [] }

    for q in questions:
        questions_by_fail[q.point_of_failure.id]['victims'].append(q.id)
    # print(questions_by_fail)
    labels = []
    body_count = []

    for key in questions_by_fail:
        labels.append(questions_by_fail[key]['title'])
        body_count.append(len(questions_by_fail[key]['victims']))

    my_obj = {
        "labels": labels,
        "data":body_count,
        "backgroundColor": ['#007bff', '#dc3545', '#ffc107', '#28a745'],
    }
    return JsonResponse(my_obj)

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



def add_section_context():
    sec_form = SectionForm()
    tag_form = TagForm()
    topic_form = TopicForm()
    context = {
            'sections': Section.objects.all().order_by('-created_at'),
            'topics': Topic.objects.all(),
            'tags': Tag.objects.all(),
            'tagForm': tag_form,
            'secForm': sec_form,
            'topicForm': topic_form 
    }
    return context
    

# @login_required(login_url='/login/') #TODO: add back in
def add_section(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        this_user = User.objects.last() #TODO: make this the user in session!!!!!!!!
        new_section = Section.objects.create(title=title, user=this_user)
        # print(new_section)
        context = add_section_context()
        context['section'] = new_section
        return render(request, 'make_charts/section_selected.html', context)
    context = add_section_context()
    return render(request, 'make_charts/section_topics_tags.html', context)

# @login_required(login_url='/login/') #TODO: add back in
def add_topic(request):
    context = add_section_context()
    if request.method == 'POST':
        # bound_form = TopicForm(request.POST)
        # print(bound_form)
        # if bound_form.is_valid():
        #     this_user = User.objects.last() #TODO: make this the user in session!!!!!!!!
        # sec = Section.objects.get(id=request.POST.get('id_section'))
        print(request.POST.get('id_section'))
        #     # tags 
        # topic = Topic.objects.create(title=request.POST['title'], section=sec)
        
        # print(topic)
        # topic.save()
    return render(request, 'make_charts/section_topics_tags.html', context)

# @login_required(login_url='/login/') #TODO: add back in
def add_tag(request):
    context = add_section_context()
    if request.method == 'POST':
        print("*"*20)
        print(request.POST['tag_title'])  #<QueryDict: 
        print(request.POST['tags_topic'])  #<QueryDict: 
                                        #{'csrfmiddlewaretoken': ['TQPBV2iCXdAvpfR0dzAJnz3egRL1Ok1QERXYX3Qc9JxGNuqeCeHfoZW6Wak0Mtex'], 
                                        #'title': ['Tag title here']}>
        # this_user = User.objects.last()
        return render(request, 'make_charts/section_topics_tags.html', context)
    
    return render(request, 'make_charts/section_topics_tags.html', context)


# def create_section(request):
#     payload = {'success': True}
#     print("hey line 44")
#     return JsonResponse(payload)


# def create_section(request):
    



# # @login_required(login_url='/login/') #TODO: add back in
# def create_section(request):
#     if request.method == 'POST':
#         bound_form = SectionForm(request.POST)
#         print("bound form *****"*4)
#         print(bound_form)
#         if bound_form.is_valid():
#             print("bound form is vailid *****"*4)
#             this_user = User.objects.last() #TODO: make this the user in session!!!!!!!!
#             Section.objects.create(title=request.POST['section_title'], user=this_user)
#             context = context = add_section_context()
#         return render(request, 'make_charts/section_topics_tags.html', context)
#     context = add_section_context()
#     return render(request, 'make_charts/section_topics_tags.html', context)