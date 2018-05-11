from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
#print(dir(django))
def index(request):
	# return HttpResponse("hello world")
	return render(request,"blog2/index.html")