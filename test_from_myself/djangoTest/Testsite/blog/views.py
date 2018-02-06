from django.shortcuts import render
from django.shortcuts import render_to_response
from . import models
# Create your views here.

def index(request):
    order_list = models.OrderList.objects.all()
    data = {}
    for row in order_list:
        data[row.name] = row.date
    return render_to_response("index.html", locals())