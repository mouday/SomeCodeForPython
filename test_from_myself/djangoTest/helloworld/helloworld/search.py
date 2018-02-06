from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators import csrf

def search_form(request):
    return render_to_response("search_form.html")


def search(request):
    # GET 方法
    request.encoding = "utf-8"
    if "q" in request.GET:
        message = "搜索内容为："+request.GET["q"]
    else:
        message = "表单为空"
    return HttpResponse(message)

def search_post(request):
    ctx={}
    if request.POST:
        ctx["rlt"] = request.POST["q"]
    return render(request, "post.html", ctx)