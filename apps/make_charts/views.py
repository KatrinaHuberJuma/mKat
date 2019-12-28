from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Section, Topic, Tag, Resource, Fail, Question, Practice, Strategy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import SectionForm, TopicForm, TagForm
from django.db.models import Count
from fractions import Fraction


# Create your views here.
# @login_required(login_url='/login/') #TODO: add back in
def dashboard(request):
    context = {
        'user': User.objects.first()
    }
    return render(request, 'make_charts/dashboard.html', context)

def pie_chart(request):
    fails = Fail.objects.all()
    questions = Question.objects.filter(answered_correctly=False)
    questions_by_fail ={ }
    # print(questions)
    # print(fails)
    for f in fails:
        questions_by_fail[f.id] = {'title': f.title, "victims": [] }

    for q in questions:
        # questions_by_fail  | question>fail id        
        questions_by_fail[q.point_of_failure.id]['victims'].append(q.id)
    # print(questions_by_fail)
    labels = []
    body_count = []

    for key in questions_by_fail:
        if not questions_by_fail[key]['title'] == "N/A":
    
            labels.append(questions_by_fail[key]['title'])
            body_count.append(len(questions_by_fail[key]['victims']))

    my_obj = {
        "labels": labels,
        "data":body_count,
    }
    return JsonResponse(my_obj)




def line_chart(request):
    # questions = Question.objects.all()
    # # pubs = Publisher.objects.annotate(num_books=Count('book'))
    # Author.objects.values('name').annotate(average_rating=Avg('book__rating'))
    practices = Practice.objects.all()
    info_dict = {}
    for p in practices:
        p_questions = p.questions.all()
        if p.date.date() not in info_dict.keys():
            info_dict[p.date.date()] = {"correct": 0, "incorrect":0, "fraction":0}
        for q in p_questions:
            if q.answered_correctly:
                info_dict[p.date.date()]['correct']+=1
            else:
                info_dict[p.date.date()]['incorrect']+=1
        
        if info_dict[p.date.date()]['incorrect'] > 0 and len(p_questions) > 0:
            info_dict[p.date.date()]['fraction'] = Fraction(info_dict[p.date.date()]['correct'], len(p_questions))
        
    labels = []
    data = []
    for key in info_dict:
        labels.append(key)
        percent_correct = int(info_dict[key]['fraction']*100)
        data.append(percent_correct)
    my_obj = {
        "labels": labels,
        "data": data,
    }
    return JsonResponse(my_obj)

# @login_required(login_url='/login/') #TODO: add back in
# def add_questions(request):
#     context = {
#         'user': User.objects.first()
#     }
#     return render(request, 'make_charts/practice_questions.html', context)


def bar_chart(request):
    questions = Question.objects.filter(answered_correctly=False)
    info_dict = {}
    for q in questions:
        q_tags = q.tags.all()
        for tag in q_tags:
            if tag not in info_dict.keys():
                info_dict[tag.id] = {"title": tag.title, "correct": 0, "incorrect":0, "fraction":0}
            if q.answered_correctly:
                info_dict[tag.id]['correct'] += 1
            else:
                info_dict[tag.id]['incorrect'] += 1
        if info_dict[tag.id]['incorrect'] > 0 and len(q_tags) > 0:
            info_dict[tag.id]['fraction'] = Fraction(info_dict[tag.id]['incorrect'], len(q_tags))
        
    labels = []
    data = []
    for key in info_dict:
        labels.append(info_dict[key]['title'])
        percent_incorrect = int(info_dict[key]['fraction']*100)
        if percent_incorrect >= 30:
            data.append(percent_incorrect)

    print(labels)
    my_obj = {
        "labels": labels,
        "data": data,
    }
    return JsonResponse(my_obj)





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
        return redirect("/add_form")
    context = add_section_context()
    return redirect("/add_form")
    
def add_form(request):
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
    return redirect("/add_form")

# @login_required(login_url='/login/') #TODO: add back in
def add_tag(request):
    context = add_section_context()
    if request.method == 'POST':
        print("*"*20)
        print('the post:')  
        print(request.POST)  # <QueryDict: {'csrfmiddlewaretoken': 
                                    # ['3hftKDhheVXqoXbCpJ8XFWWaEvhbU6aoo1JW8jYJkZVvG6CJGAVpkd28Mc97EeWq'], 
                                    # 'tag_title': ['three 51'], 
                                    # 'tags_topic': ['28', '30', '31']}>
        print("*"*20)
        print("*"*20)
        topic_ids = [int(topic_id) for topic_id in request.POST.getlist("tag_topics")]
        print(topic_ids)
        tag = Tag.objects.create(title=request.POST['tag_title'])
        for topic_id in topic_ids:
            tag.topics.add(topic_id)
        tag.save()
        print(tag.topics.all())
        return render(request, 'make_charts/register.html', context)
    
    return redirect("/add_form")

# def create_section(request):
#     payload = {'success': True}
#     print("hey line 44")
#     return JsonResponse(payload)


# def create_section(request):
    



@login_required(login_url='/login/') #TODO: add back in
def create_section(request):
    if request.method == 'POST':
        bound_form = SectionForm(request.POST)
        print("bound form *****"*4)
        print(bound_form)
        if bound_form.is_valid():
            print("bound form is vailid *****"*4)
            this_user = User.objects.last() #TODO: make this the user in session!!!!!!!!
            Section.objects.create(title=request.POST['section_title'], user=this_user)
            context = context = add_section_context()
        return redirect("/add_form")
    context = add_section_context()
    return render(request, 'make_charts/section_topics_tags.html', context)