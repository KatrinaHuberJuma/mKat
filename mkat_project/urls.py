"""mkat_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.make_charts.models import Fail, Section, Resource, Practice, Topic, Question, Tag, Strategy
from apps.login_app.models import User as U
class UAdmin(admin.ModelAdmin):
    pass
admin.site.register(U, UAdmin)

class FailAdmin(admin.ModelAdmin):
    pass
admin.site.register(Fail, FailAdmin)

class SectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Section, SectionAdmin)

class ResourceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Resource, ResourceAdmin)

class PracticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Practice, PracticeAdmin)

class TopicAdmin(admin.ModelAdmin):
    pass
admin.site.register(Topic, TopicAdmin)

class QuestionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Question, QuestionAdmin)

class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)

class StrategyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Strategy, StrategyAdmin)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.make_charts.urls')),
    url(r'^login/', include('apps.login_app.urls')),
]
