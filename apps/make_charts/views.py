from django.shortcuts import render
from ..login_app.models import User
from django.contrib.auth.decorators import login_required


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
    context = {
        'user': User.objects.first()
    }
    return render(request, 'make_charts/section_topics_tags.html', context)
