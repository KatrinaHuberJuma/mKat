from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^add_questions$', views.add_questions),
    url(r'^add_practice$', views.add_practice),
]