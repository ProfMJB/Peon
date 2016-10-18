from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def add(request):
    return HttpResponse('<title>Add Peon</title>')