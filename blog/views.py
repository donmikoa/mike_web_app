from django.shortcuts import render
from django.http import HttpResponse

# Creating the views

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')

