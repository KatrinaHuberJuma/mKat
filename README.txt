TODO in mkat_project/mkat_project/: 
	
 _____________ in mkat_project/settings.py,  INSTALLED_APPS list 
	
 __________________________'apps.make_charts', 
	
 _____________ in urls.py:  
	
 __________________________ comment out, or just delete 'from django.contrib import admin'
	
 __________________________url(r'^', include('apps.make_charts.urls')),	# add to url patterns, don't forget the comma 
	TODO in mkat_project/appsmake_charts/: 
	
 _____________ in urls.py:
	
 __________________________ from django.conf.urls import url
	
 __________________________ from . import views
	
 __________________________in urlpatterns add
	
 ________________________________________ url(r'^$', views.index), # index is the name of a method in views.py
	
 _____________ in views.py:
	
 __________________________from django.shortcuts import render, redirect
	
 __________________________def index(request):
	
 __________________________    return render(request, 'make_charts/index.html')
