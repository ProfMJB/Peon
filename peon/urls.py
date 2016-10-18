'''
Created on 18 Oct 2016

@author: Max
'''
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^add/', views.add, name = 'add'),
]

