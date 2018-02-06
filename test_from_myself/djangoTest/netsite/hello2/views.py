from django.shortcuts import render

# Create your views here.

def show_time(request):
    return render(request, "showtime.html")  # 打包函数