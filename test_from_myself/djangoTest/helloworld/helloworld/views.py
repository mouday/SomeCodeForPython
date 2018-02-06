from django.http import HttpResponse
from django.shortcuts import render
import time

def hello(request):
    return HttpResponse("hello world!") 

def sayhello(request):
    context={}
    context["hello"]="hello,world!"
    return render(request, "hello.html", context)

def label(request):
    context={}
    context["condition1"]=True
    context["condition2"]=True
    context["items"]=["item1","item2","item3"]
    context["one"]="one"
    context["two"]="two"
    context["name"]="tom"
    context["address"]="beijing"
    context["currenttime"]=time.strftime("%Y-%m-%d")
    return render(request, "label.html", context)

def child(request):
    context={}
    return render(request, "child.html", context)