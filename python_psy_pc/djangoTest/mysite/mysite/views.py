from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<html>hello world</html>")

def show_list(request):
    return HttpResponse("blog_list")

def show_blog(request):
    return HttpResponse("blog")