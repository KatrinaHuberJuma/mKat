from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard),
    # url(r'^add_questions$', views.add_questions),
    url(r'^add_practice$', views.add_practice),
    url(r'^section/add$', views.add_section),
    # url(r'^section/create$', views.create_section),
]