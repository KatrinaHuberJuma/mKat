# login_app APP LEVEL URLS
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.root),
    url(r'^login$', views.login),
    url(r'^new$', views.reg),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
]
