from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_time),
    path("message/", views.message)
]
