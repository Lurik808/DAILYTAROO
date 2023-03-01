
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/<str:name>", views.about, name='about')
]
